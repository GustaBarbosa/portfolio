"""Portfolio web app.

Run locally:  uvicorn app.main:app --reload
Then open:    http://localhost:8000
"""

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.data import EXPERIENCE, PROFILE, PROJECTS, SKILLS

STATIC_DIR = Path(__file__).parent / "static"

app = FastAPI(title="Portfolio API", version="0.1.0")

# Serves style.css, script.js and any images from app/static/ under /static/...
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/", include_in_schema=False)
def index() -> FileResponse:
    """The portfolio page itself."""
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/health")
def health() -> dict:
    """Used later by Docker and Kubernetes to check the app is alive."""
    return {"status": "ok"}


@app.get("/api/profile")
def profile() -> dict:
    return PROFILE


@app.get("/api/skills")
def skills() -> list[dict]:
    return SKILLS


@app.get("/api/experience")
def experience() -> list[dict]:
    return EXPERIENCE


@app.get("/api/projects")
def projects() -> list[dict]:
    return PROJECTS
