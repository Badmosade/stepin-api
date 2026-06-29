from fastapi import FastAPI
from dotenv import load_dotenv
from app.core.database import engine, Base
from app.models import category, state, resource, certification
from app.routers import categories, states, resources


load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="StepIn API",
    description="Helping immigratants find resources across the United States",
    version="1.0.0"
)

app.include_router(categories.router)
app.include_router(states.router)
app.include_router(resources.router)


@app.get("/")
def home():
    return {
        "message": "Welcome to the StepIn API!",
        "description": "Helping immigratants find resources across the United States"
    }


@app.get("/health")
def health():
    return {"status": "ok"}
