from fastapi import APIRouter

router = APIRouter()

@router.get("/entities")
async def list_entities():
    return {"entities": []}

@router.get("/entities/{entity_id}")
async def get_entity(entity_id: str):
    return {"entity_id": entity_id}