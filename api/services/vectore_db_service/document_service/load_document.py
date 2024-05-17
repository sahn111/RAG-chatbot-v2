from langchain_community.document_loaders import CSVLoader

DATA_PATH = "data/TCT_first_items.csv"

def load_documents():
    document_loader = CSVLoader(DATA_PATH)
    return document_loader.load()
