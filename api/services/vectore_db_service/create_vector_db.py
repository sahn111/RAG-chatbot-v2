import argparse
import os
import shutil
from langchain.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from langchain_community.vectorstores import Chroma

from .document_service import *

def create_vector_database():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="Reset the database.")
    args = parser.parse_args()
    if args.reset:
        clear_database()

    documents = load_documents()
    chunks = split_documents(documents)
    add_to_chroma(chunks)