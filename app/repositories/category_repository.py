from sqlalchemy.orm import Session
from app.models.model_category import Category


def create_category(database: Session, name_category, id):
    new_category = Category(name_category=name_category, id=id)
    database.add(new_category)
    database.commit()
    database.refresh(new_category)


def get_all_category(database: Session):
    categories = database.query(Category).all()
    return categories


def get_category_by_id(id: int, database: Session):
    category = database.query(Category).filter(Category.id == id).first()
    return category


def update_category(database: Session, id: int, name_category: str):
    category = get_category_by_id(database=database, id=id)
    if not category:
        return None
    else:
        category.name_category = name_category
        database.commit()
        database.refresh(category)
        return category


def delete_category(database: Session, id:int):
    category = get_category_by_id(database=database, id=id)
    if not category:
        return False
    else:
        database.delete(category)
        database.commit()
        return True

