from sqlalchemy.orm import Session, defer, undefer_group
from app.models.product_model import Product, ProductResponse, ProductRequest


def insert(database: Session, product: ProductRequest):
    product = Product(name=product.name, description=product.description, price=product.price)
    database.add(product)
    database.commit()
    return ProductResponse(id=product.id, name=product.name, description=product.description, price=product.price)


def get_all(database: Session):
    query = database.query(Product)
    query = query.options(defer('created_at'), defer('updated_at'))
    products = query.all()
    return products


def get_by_id(id: int, database: Session):
    query = database.query(Product)
    query = query.options(defer('created_at'), defer('updated_at'))
    product = query.filter(Product.id == id).first()
    return product


def update(database: Session, payload: ProductRequest, id: int):
    product = get_by_id(database=database, id=id)
    if product:
        product.name = payload.name
        product.description = payload.description
        product.price = payload.price
        database.commit()
        database.refresh(product)
        return ProductResponse(id=product.id, name=product.name, description=product.description, price=product.price)
    else:
        return False


def delete(database: Session, id: int):
    product = get_by_id(database=database, id=id)
    if product:
        database.delete(product)
        database.commit()
        return True
    else:
        return False
