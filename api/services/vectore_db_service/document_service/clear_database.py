import os
import shutil

CHROMA_PATH = "chroma"

def clear_database():
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

