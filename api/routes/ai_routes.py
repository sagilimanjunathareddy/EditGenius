from fastapi import APIRouter
from ai_engine.ai_writer import generate_content
from ai_engine.ai_reviewer import refine_text

router = APIRouter()

@router.post("/ai/rewrite")
def ai_rewrite(text: str, prompt: str = None):
    return {"rewritten": generate_content(text, prompt)}

@router.post("/ai/review")
def ai_review(text: str, prompt: str):
    return {"reviewed": refine_text(text, prompt)}
