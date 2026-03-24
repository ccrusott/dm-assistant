from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class IngestRequest(BaseModel):
    text: str
    session_id: str | None = None

@router.post("/")
async def ingest_notes(body: IngestRequest):
    # Extraction agent will live here
    return {"received": body.text, "status": "extraction pending"}