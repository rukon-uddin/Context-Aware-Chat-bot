"""
Download the embedding model first, using the below command
git clone https://huggingface.co/CompendiumLabs/bge-base-en-v1.5-gguf
"""

from llm_system import ChatGPTClient
from rag_system import SimpleRag

rag = SimpleRag()
client = ChatGPTClient()

rag.process_data()

while True:
    input_query = input('Ask me a question: ')
    if input_query == "q":
        break
    retrieved_knowledge = rag.match_context(input_query)
    print(retrieved_knowledge)

    print('Retrieved knowledge:')
    for chunk, similarity in retrieved_knowledge:
        print(f' - (similarity: {similarity:.2f}) {chunk}')

    context_formatted = '\n'.join([f'- {chunk}' for chunk, similarity in retrieved_knowledge])
    instruction_prompt = f"""You are a helpful chatbot.
    Use only the following pieces of context to answer the question. Don't make up any new information:
    {context_formatted}
    """

    message_format = [
    {"role": "system", "content": instruction_prompt},
    {"role": "user", "content": input_query}
    ]

    gptResp = client.ask(message_format)
    print("GPT Response: ", gptResp)
    print("\n\n")