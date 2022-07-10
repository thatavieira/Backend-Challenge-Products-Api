from fastapi import HTTPException
from sqlalchemy.orm import Session, defer
from app.models.product_model import Product, ProductResponse, ProductRequest
from sqlalchemy import func


def add(database: Session, product: ProductRequest):
    try:
        product = Product(
            name=product.name,
            description=product.description,
            price=product.price,
            category_id=product.category_id)
        database.add(product)
        database.commit()
        database.refresh(product)
        return ProductResponse(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
            category_id=product.category_id)
    except Exception as e:
        custom_alchemy_exception(e)


def get_all(database: Session):
    try:
        query = database.query(Product)
        query = query.options(defer('created_at'), defer('updated_at'))
        products = query.all()
        return products
    except Exception as e:
        custom_alchemy_exception(e)


def get_by_id(id: int, database: Session):
    try:
        product = database.query(Product).filter(Product.id == id).first()
        product_is_not_exist = not isinstance(product, Product)

        if product_is_not_exist:
            print(product_is_not_exist)
            raise Exception(f"product {id} not exist")

        return ProductResponse(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
            category_id=product.category_id)
    except Exception as e:
        custom_alchemy_exception(e)


def update(database: Session, payload: ProductRequest, id: int):
    try:
        product = get_by_id(database=database, id=id)
        product.name = payload.name
        product.description = payload.description
        product.price = payload.price
        product.updated_at = func.now()
        database.commit()
        database.refresh(product)
        return ProductResponse(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
            category_id=product.category_id)
    except Exception as e:
        print(e)
        custom_alchemy_exception(e)


def delete(database: Session, id: int):
    try:
        product = database.query(Product).filter_by(id=id).first()
        product_is_not_exist = not isinstance(product, Product)

        if product_is_not_exist:
            print(product_is_not_exist)
            raise Exception(f"product {id} not exist")

        database.delete(product)
        database.commit()
        return ProductResponse(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
            category_id=product.category_id)
    except Exception as e:
        custom_alchemy_exception(e)


def custom_alchemy_exception(e):
    raise HTTPException(status_code=400, detail=f"{e.args}")