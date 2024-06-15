# 翻译模块
from fastapi import  APIRouter
from ..gpt import get_english, get_chinese, academic_paper_refinement, writing_guidance_and_refinement, generate_sentences

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

@router.post("/academic_paper")
async def academic_paper(
    text: str,
):
    return academic_paper_refinement(text)

@router.post("/write")
async def write(
    text: str,
):
    return writing_guidance_and_refinement(text)

@router.post("/word")
async def word(
    word: str,
):
    return generate_sentences(word)