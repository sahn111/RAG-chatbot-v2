import argparse
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama

from .document_service import get_embedding_service
CHROMA_PATH = "chroma"

def query_rag(query_text: str):
    embedding_function = get_embedding_service()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    results = db.similarity_search_with_score(query_text, k=2)
    return results