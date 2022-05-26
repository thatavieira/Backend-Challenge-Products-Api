from fastapi import APIRouter
from app.repositories import product_repository
import app.models.model_product as model_product
from app.database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends

model_product.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_product(name_product: str, id: int, database: Session = Depends(get_db)):
    product = product_repository.create_product(database=database, name_product=name_product, id=id)
    return {"product": product}


@router.get("/")
def get_all_product(database: Session = Depends(get_db)):
    product = product_repository.get_all_product(database=database)
    return {"products": product}


@router.get("/{id}")
def get_product_by_id(id: int, database: Session = Depends(get_db)):
    product = product_repository.get_product_by_id(database=database, id=id)
    return {"product": product}


@router.put("/")
def update_product(id: int, name_product: str, database: Session = Depends(get_db)):
    product = product_repository.update_product(database=database, id=id, name_product=name_product)
    if product:
        return product
    else:
        return {"error": f"Product with id {id} does not exist"}


@router.delete("/")
def delete_product(id: int, database: Session = Depends(get_db)):
    is_removed = product_repository.delete_product(database=database, id=id)
    if is_removed:
        return {"message": f"product {id} removed"}
    else:
        return {"error": f"product with id {id} does not exist"}

