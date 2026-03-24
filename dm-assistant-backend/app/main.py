from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import health, ingest, wiki, prep

app = FastAPI(title=settings.app_name, debug=settings.debug)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(ingest.router, prefix="/ingest", tags=["ingest"])
app.include_router(wiki.router, prefix="/wiki", tags=["wiki"])
app.include_router(prep.router, prefix="/prep", tags=["prep"])