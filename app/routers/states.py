from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.state import State

router = APIRouter(
    prefix="/states",
    tags=["States"]
)


@router.get("/")
def get_states(db: Session = Depends(get_db)):
    states = db.query(State).all()
    return states


@router.get("/{state_id}")
def get_state(state_id: int, db: Session = Depends(get_db)):
    state = db.query(State).filter(State.id == state_id).first()
    return state
