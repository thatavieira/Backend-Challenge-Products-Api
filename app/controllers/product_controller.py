from fastapi import APIRouter, HTTPException
from app.repositories import product_repository as repository
import app.models.product_model as model_product


from app.models.product_model import Product, ProductRequest, ProductResponse
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


@router.post("/", response_model=ProductResponse)
def create(product: ProductRequest, database: Session = Depends(get_db)):
    product = repository.insert(database=database, product=product)
    return product


@router.get("/", response_model_include=ProductResponse, response_model_exclude=Product)
def get_all(database: Session = Depends(get_db)):
    return repository.get_all(database=database)


@router.get("/{id}")
def get_by_id(id: int, database: Session = Depends(get_db)):
    product = repository.get_by_id(database=database, id=id)

    if product:
        return product
    else:
        raise HTTPException(status_code=404, detail=f"Id {id} not found")


@router.put("/{id}")
def update(product: ProductRequest, id: int, database: Session = Depends(get_db)):
    product = repository.update(database=database, payload=product, id=id)
    if product:
        return product
    else:
        return product


@router.delete("/{id}")
def delete(id: int, database: Session = Depends(get_db)):
    is_removed = repository.delete(database=database, id=id)
    if is_removed:
        return {"message": f"product {id} removed"}
    else:
        return {"error": f"product with id {id} does not exist"}

