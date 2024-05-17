from sentence_transformers import SentenceTransformer

def get_embedding_model_service():
    model = SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L6-v2')
    return model