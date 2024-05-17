import requests
import json

from langchain.prompts import ChatPromptTemplate

from models import QuestionModel

from ..vectore_db_service.get_from_db import *

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
 - You are a good lawyer who lives in turkey.

 - Answer the question only in turkish language.
 
Answer the question based only on the following context:

{context}

---

Answer the question in turkish only based on the above context: {question}
"""

def get_relevant_laws_service(question : QuestionModel):
    results = query_rag(question.question)
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=question.question)

    print("--------------------------------", prompt)

    url = "https://api.awanllm.com/v1/completions"
    payload = json.dumps({
    "model": "Meta-Llama-3-8B-Instruct",
    "prompt": f"{prompt}"
    })
    
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f"Bearer d3de4afa-35c6-4fcb-9738-de706606389d"
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response_json = response.json()

    message = str(response_json["choices"][0]["text"]).strip()
    message = message.replace("\n", " ")
    return message.replace("\\", "")