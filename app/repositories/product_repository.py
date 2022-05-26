from sqlalchemy.orm import Session
from app.models.model_product import Product


def create_product(database: Session, name_product: str, id: int):
    product = Product(name_product=name_product, id=id)
    database.add(product)
    database.commit()
    database.refresh(product)


def get_all_product(database: Session):
    products = database.query(Product).all()
    return products


def get_product_by_id(id: int, database: Session):
    product = database.query(Product).filter(Product.id == id). first()
    return product


def update_product(database: Session, id:int, name_product: str):
    product = get_product_by_id(database=database, id=id)
    if not product:
        return None
    else:
        product.name_product = name_product
        database.commit()
        database.refresh(product)
        return product


def delete_product(database: Session, id: int):
    product = get_product_by_id(database=database, id=id)
    if not product:
        return False
    else:
        database.delete(product)
        database.commit()
        return True