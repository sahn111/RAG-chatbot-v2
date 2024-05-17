from fastapi import APIRouter
from models import QuestionModel
from ..services import get_relevant_laws_service, get_inferenced_laws_service

router = APIRouter(
    prefix="/law",
    tags=["Law"],
    responses={404: {"description": "Not found"}},
)

@router.post("/relevant_laws")
async def get_relevant_laws_router(
    question: QuestionModel
):
    return get_relevant_laws_service(question)

@router.post("/inferenced")
async def get_inferenced_law(
        question : QuestionModel
):
    return get_inferenced_laws_service(question)