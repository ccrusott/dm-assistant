from fastapi import APIRouter

router = APIRouter()

@router.get("/session/{session_id}")
async def get_session_brief(session_id: str):
    # Context assembly agent will live here
    return {"session_id": session_id, "brief": "prep agent pending"}
