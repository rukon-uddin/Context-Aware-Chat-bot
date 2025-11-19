from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Tuple
from llm_system import ChatGPTClient
from rag_system import SimpleRag

app = FastAPI(title="RAG Chat API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize RAG system and ChatGPT client
rag = SimpleRag()
client = ChatGPTClient()

# Process data on startup
@app.on_event("startup")
async def startup_event():
    print("Processing RAG data...")
    rag.process_data()
    print("RAG system ready!")


class ChatRequest(BaseModel):
    query: str


class ContextItem(BaseModel):
    chunk: str
    similarity: float


class ChatResponse(BaseModel):
    response: str
    retrieved_context: List[ContextItem]


@app.get("/")
async def root():
    return {
        "message": "RAG Chat API is running",
        "endpoints": {
            "chat": "/chat (POST)",
            "health": "/health (GET)"
        }
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Process a chat query using RAG system
    """
    try:
        if not request.query.strip():
            raise HTTPException(status_code=400, detail="Query cannot be empty")

        # Retrieve relevant context
        retrieved_knowledge = rag.match_context(request.query)
        
        # Format context for the prompt
        context_formatted = '\n'.join([f'- {chunk}' for chunk, similarity in retrieved_knowledge])
        
        # Create instruction prompt
        instruction_prompt = f"""You are a helpful chatbot.
        Use only the following pieces of context to answer the question. Don't make up any new information:
        {context_formatted}
        """
        
        # Prepare message format for ChatGPT
        message_format = [
            {"role": "system", "content": instruction_prompt},
            {"role": "user", "content": request.query}
        ]
        
        # Get response from ChatGPT
        gpt_response = client.ask(message_format)
        
        # Format retrieved context for response
        context_items = [
            ContextItem(chunk=chunk, similarity=float(similarity))
            for chunk, similarity in retrieved_knowledge
        ]
        
        return ChatResponse(
            response=gpt_response,
            retrieved_context=context_items
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)