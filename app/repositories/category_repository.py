from sqlalchemy.orm import Session, defer
from sqlalchemy import func
from app.models.category_model import Category, CategoryResponse, CategoryRequest
from fastapi import HTTPException


def add(database: Session, name: str):
    try:
        category = Category(name=name)
        database.add(category)
        database.commit()
        database.refresh(category)
        return CategoryResponse(id=category.id, name=category.name)
    except Exception as e:
        custom_alchemy_exception(e)


def get_all(database: Session):
    try:
        query = database.query(Category)
        query = query.options(defer('created_at'), defer('updated_at'))
        category = query.all()
        return category
    except Exception as e:
        custom_alchemy_exception(e)


def get_by_id(id: int, database: Session):
    try:
        category = database.query(Category).filter_by(id=id).first()
        category_is_not_exist = not isinstance(category, Category)

        if category_is_not_exist:
            raise Exception(f"category {id} not exist")

        return CategoryResponse(
            id=category.id,
            name=category.name)
    except Exception as e:
        custom_alchemy_exception(e)


def update(database: Session, category: CategoryRequest, id: int):
    try:
        update_category = database.query(Category).filter_by(id=id).first()
        category_is_not_exist = not isinstance(update_category, Category)

        if category_is_not_exist:
            raise Exception(f"category {id} not exist")

        update_category = get_by_id(database=database, id=id)
        update_category.name = category.name
        database.commit()
        return CategoryResponse(
            id=update_category.id,
            name=update_category.name)
    except Exception as e:
        custom_alchemy_exception(e)


def delete(database: Session, id: int):
    try:
        category = database.query(Category).filter_by(id=id).first()
        category_is_not_exist = not isinstance(category, Category)

        if category_is_not_exist:
            raise Exception(f"category {id} not exist")

        database.delete(category)
        database.commit()
        return CategoryResponse(
            id=category.id,
            name=category.name)
    except Exception as e:
        custom_alchemy_exception(e)


def custom_alchemy_exception(e):
    raise HTTPException(status_code=400, detail=f"{e.args}")