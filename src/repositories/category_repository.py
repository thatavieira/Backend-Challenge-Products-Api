from src.repositories import *
from src.models.category_model import Category, CategoryResponse, CategoryRequest


def add(database: Session, name: str):
    try:
        category = Category(name=name)
        database.add(category)
        database.commit()
        database.refresh(category)
        return category
    except Exception as e:
        custom_alchemy_exception(e)


def get_all(database: Session):
    try:
        return paginate(database.query(Category))
    except Exception as e:
        custom_alchemy_exception(e)


def get_by_id(id: int, database: Session):
    try:
        category = database.query(Category).filter_by(id=id).first()
        category_is_not_exist = not isinstance(category, Category)

        if category_is_not_exist:
            raise Exception(f"category {id} not exist")

        return CategoryResponse.from_orm(category)
    except Exception as e:
        custom_alchemy_exception(e)


def update(database: Session, category: CategoryRequest, id: int):
    try:
        update_category = database.query(Category).filter_by(id=id).first()
        category_is_not_exist = not isinstance(update_category, Category)

        if category_is_not_exist:
            raise Exception(f"category {id} not exist")

        update_category.name = category.name
        update_category.updated_at = func.now()
        database.commit()
        database.refresh(update_category)
        return CategoryResponse.from_orm(update_category)
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
        return CategoryResponse.from_orm(category)
    except Exception as e:
        custom_alchemy_exception(e)


def custom_alchemy_exception(e):
    raise HTTPException(status_code=400, detail=f"{e.args}")