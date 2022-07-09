from fastapi import APIRouter
from app.repositories import category_repository
import app.models.category_model as model_category
from app.database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends

model_category.Base.metadata.create_all(bind=engine)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_category(name_category: str, id: int, database: Session = Depends(get_db)):
    category = category_repository.create_category(database=database, name_category=name_category, id=id)
    return {"category": category}

@router.get("/")
def get_all_category(database: Session = Depends(get_db)):
    category = category_repository.get_all_category(database=database)
    return {"categories": category}


@router.get("/{id}")
def get_category_by_id(id: int, database: Session = Depends(get_db)):
    category = category_repository.get_category_by_id(database=database, id=id)
    return {"category": category}

@router.put("/")
def update_category(id: int, name_category: str, database: Session = Depends(get_db)):
    category = category_repository.update_category(database=database, id=id, name_category=name_category)
    if category:
        return category
    else:
        return {"error": f"Category with id {id} does not exist"}

@router.delete("/")
def delete_category(id: int, database: Session = Depends(get_db)):
    is_removed = category_repository.delete_category(database=database, id=id)
    if is_removed:
        return {"message": f"category {id} removed"}
    else:
        return {"error": f"category with id {id} does not exist"}