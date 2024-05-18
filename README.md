# Embedding Service with FastAPI and Chroma

# Overview
This is a RAG App project. By using a CSV file, I created a chatbot that returns answers about law questions. 

# File Structure

- Routers
    This is the first point where our API interacts with the outer world.
    We manage service functions in these files.

- Services
    This is the smart file of the project. We do all logic work here, it consists creating a vectorstore,
    returning a understandable answer or reading the document etc.

- Models
    We keep our input models here. Actually, we can add database models, but we do not use a relational DB here.

    Loading document with chunk operation is inspired by Langchain Documentation (https://python.langchain.com/v0.1/docs/integrations/document_loaders/docugami/#advantages-vs-other-chunking-techniques)


# LLM Model
I used " Llama-3 " for llm model. And I used " nomic-embed-text " for creating embeddings. 

Awan LLM is used for to increase performance, because of my local computer's hardware, it was very slow to generate answer from llama3
so that I used Awan LLM API to generate answer from llama.

Check out Awan LLM documentation -> https://www.awanllm.com/docs

# Database
Choroma Db is used for vector store



# How to run?

## Running the service on debug mode
1. Run the FastAPI service:
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

## Dockerization
1. Build the Docker image:
    ```bash
    docker build -t law-service .
    ```

2. Run the Docker container:
    ```bash
    docker run -d -p 8000:8000 law-service
    ```