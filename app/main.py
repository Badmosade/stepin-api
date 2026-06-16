from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

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
