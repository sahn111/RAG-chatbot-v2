import faiss
import numpy as np
import pandas as pd
import requests
import json

from fastapi import HTTPException
from models import QuestionModel
from ..embedding_model import get_embedding_model_service

def get_relevant_laws_service(question : QuestionModel):
    model = get_embedding_model_service()

    index = faiss.read_index("laws_index.faiss")
    df = pd.read_pickle("laws_dataframe.pkl")

    try:
        query_embedding = model.encode([question.question])
        k = 2
        _, indices = index.search(np.array(query_embedding), k)        
        relevant_laws = df.iloc[indices[0]].to_dict(orient='records')
        return {"relevant_laws": relevant_laws}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_inferenced_laws_service(question : QuestionModel):
    model = get_embedding_model_service()

    index = faiss.read_index("laws_index.faiss")
    df = pd.read_pickle("laws_dataframe.pkl")

    try:
        query_embedding = model.encode([question.question])
        k = 2
        _, indices = index.search(np.array(query_embedding), k)        
        relevant_laws = df.iloc[indices[0]].to_dict(orient='records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


    url = "https://api.awanllm.com/v1/chat/completions"
    payload = json.dumps({
        "model": "Awanllm-Llama-3-8B-Dolfin",
        "messages": [
            {
                "role": "user",
                "content": f"Could you please clarify these two legal statements for the user? Relevant laws: {relevant_laws}"
            },
            {
                "role": "assistant",
                "content": "The assistant will respond in Turkish."
            }
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f"Bearer d3de4afa-35c6-4fcb-9738-de706606389d	"
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response_json = response.json()
    message = response_json["choices"][0]["message"]["content"]
    return message.replace("\n", " ")