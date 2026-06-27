from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.category import Category

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


@router.get("/")
def get_categories(db: Session = Depends(get_db)):
    categories = db.query(Category).all()
    return categories


@router.post("/")
def create_category(name: str, description: str = None, db: Session = Depends(get_db)):
    category = Category(name=name, description=description)
    db.add(category)
    db.commit()
    db.refressh(category)
    return category
