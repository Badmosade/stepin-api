from fastapi import FastAPI
from dotenv import load_dotenv
from app.core.database import engine, Base
from app.models import category, state, resource, certification

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="StepIn API",
    description="Helping immigratants find resources across the United States",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to the StepIn API!",
        "description": "Helping immigratants find resources across the United States"
    }


@app.get("/health")
def health():
    return {"status": "ok"}
