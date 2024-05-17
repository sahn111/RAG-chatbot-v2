# Embedding Service with FastAPI and FAISS

## Overview
This project provides a FastAPI service for retrieving the most relevant legal texts based on cosine similarity of embeddings using FAISS for efficient vector storage and retrieval.


## Data Preparation
1. Prepare the embeddings and store them in a FAISS index

## Running the Service
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