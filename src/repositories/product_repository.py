from fastapi import HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import func
from sqlalchemy.orm import Session, joinedload
from src.models.product_model import Product, ProductRequest, ProductResponse


def add(database: Session, product: ProductRequest):
    try:
        product = Product(product)
        database.add(product)
        database.commit()
        database.refresh(product)
        return ProductResponse.from_orm(product)
    except Exception as e:
        custom_alchemy_exception(e)


def get_all(database: Session):
    try:
        return paginate(database.query(Product).options(joinedload(Product.category)))
    except Exception as e:
        custom_alchemy_exception(e)


def get_by_id(id: int, database: Session):
    try:
        query = database.query(Product)
        query = query.options(joinedload(Product.category))
        product = query.filter(Product.id == id).first()
        product_is_not_exist = not isinstance(product, Product)

        if product_is_not_exist:
            print(product_is_not_exist)
            raise Exception(f"product {id} not exist")

        return ProductResponse.from_orm(product)
    except Exception as e:
        custom_alchemy_exception(e)


def update(database: Session, payload: ProductRequest, id: int):
    try:
        update_product = database.query(Product).filter_by(id=id).first()
        product_is_not_exist = not isinstance(update_product, Product)

        if product_is_not_exist:
            raise Exception(f"product {id} not exist")

        update_product.name = payload.name
        update_product.description = payload.description
        update_product.price = payload.price
        update_product.updated_at = func.now()
        database.commit()
        database.refresh(update_product)
        return ProductResponse.from_orm(update_product)
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
        return ProductResponse.from_orm(product)
    except Exception as e:
        custom_alchemy_exception(e)


def custom_alchemy_exception(e):
    raise HTTPException(status_code=400, detail=f"{e.args}")
