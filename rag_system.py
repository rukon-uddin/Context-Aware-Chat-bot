# import ollama
from utils import MyUtils
from llama_cpp import Llama

class SimpleRag:
    def __init__(self):
        self.embedding_model_url = './bge-base-en-v1.5-gguf/bge-base-en-v1.5-f16.gguf'
        self.dataset = []
        self.VECTOR_DB = []
        self.model = Llama(self.embedding_model_url, embedding=True)
        self.util = MyUtils()
    

    def get_embeddings(self, data):
        embedding = self.model.embed(data)
        return embedding


    def match_context(self, query, limit = 3):
        query_embedding = self.model.embed(query)
        similarities = []
        for chunk, embedding in self.VECTOR_DB:
            similarity = self.util.cosine_similarity(query_embedding, embedding)
            similarities.append((chunk, similarity))
        
        similarities.sort(key=lambda x: x[1], reverse=True)
        
        return similarities[:limit]
    
    def process_data(self):
        print("Loading Data ...")
        with open('cat.txt', 'r') as file:
            self.dataset = file.readlines()
            print(f'Loaded {len(self.dataset)} entries')
        print("Saving Embeddings ...")
        for i, data in enumerate(self.dataset):
            embeding = self.get_embeddings(data)
            self.VECTOR_DB.append((data, embeding))
            print(f'Added data {i+1}/{len(self.dataset)} to the database')    

    def get_vector_db(self):
       return self.VECTOR_DB
    
    def get_dataset(self):
       return self.dataset

