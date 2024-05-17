import time

from fastapi import FastAPI, Request

from api.routers import law_router
from api.services import create_vector_database
app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    return response


app.include_router(law_router.router)

@app.get("/")
async def root():
    return {"message": "Welcome to RAG APP API!"}

if __name__ == "__main__":
    import uvicorn
    create_vector_database()
    uvicorn.run(app, host="0.0.0.0", port=8000)