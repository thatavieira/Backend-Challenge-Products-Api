from sqlalchemy import Column, Integer, String
from app.database import Base


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name_category = Column(String(20))

