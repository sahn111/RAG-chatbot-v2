import pandas as pd
import numpy as np
import faiss

from ..embedding_model import get_embedding_model_service

def create_vector_database():
    model = get_embedding_model_service()

    df = pd.read_csv('~/RAG-chatbot-v2/csv_store/TCT_first_items.csv')
    texts = df['text'].tolist()
    embeddings = model.encode(texts)
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    faiss.write_index(index, "laws_index.faiss")
    df.to_pickle("laws_dataframe.pkl")
    return True 