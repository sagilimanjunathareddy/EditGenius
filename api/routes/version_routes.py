from fastapi import APIRouter
from storage.version_control import save_version, load_version

router = APIRouter()

@router.post("/version/save")
def save(doc_id: str, content: str):
    save_version(doc_id, content)
    return {"status": "saved"}

@router.get("/version/load")
def load(doc_id: str):
    content = load_version(doc_id)
    return {"content": content}
