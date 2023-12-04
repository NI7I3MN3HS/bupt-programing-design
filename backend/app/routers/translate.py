# 翻译模块
from fastapi import  APIRouter
from ..gpt import get_english, get_chinese

router = APIRouter(prefix="/translate", tags=["translate"])

@router.post("/english2chinese")
async def english2chinese(
    text: str,
):
    return get_english(text)
    

@router.post("/chinese2english")
async def chinese2english(
    text: str,
):
    return get_chinese(text)