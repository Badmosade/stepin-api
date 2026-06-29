from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.resource import Resource

router = APIRouter(
    prefix="/resources",
    tags=["Resources"]
)


@router.get("/")
def get_resources(db: Session = Depends(get_db)):
    resources = db.query(Resource).all()
    return resources


@router.get("/{resource_id}")
def get_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = db.query(Resource).filter(Resource.id == resource_id).first()
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource


@router.get("/state/{state_id}")
def get_resources_by_state(state_id: int, db: Session = Depends(get_db)):
    resources = db.query(Resource).filter(Resource.state_id == state_id).all()
    return resources


@router.get("/category/{category_id}")
def get_resources_by_category(category_id: int, db: Session = Depends(get_db)):
    resources = db.query(Resource).filter(
        Resource.category_id == category_id).all()
    return resources


@router.post("/")
def create_resource(
    name: str,
    state_id: int,
    category_id: int,
    description: str = None,
    address: str = None,
    phone: str = None,
    website: str = None,
    db: Session = Depends(get_db)
):
    resource = Resource(
        name=name,
        description=description,
        address=address,
        phone=phone,
        website=website,
        state_id=state_id,
        category_id=category_id
    )
    db.add(resource)
    db.commit()
    db.refresh(resource)
    return resource
