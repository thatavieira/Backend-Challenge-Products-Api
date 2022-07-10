from uuid import UUID
from typing import Union
from app.database import Base
from sqlalchemy import Column, String, Float, ForeignKey, Integer
from app.models.base_model import BaseModel
from pydantic import Field, BaseModel as PydanticBaseModel
from .category_model import Category
from sqlalchemy.orm import relationship


class Product(BaseModel, Base):
    __tablename__ = 'products'

    name = Column(String(50), nullable=False, index=True, unique=True)
    description = Column(String(50), nullable=False)
    price = Column(Float)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship(Category)


class ProductRequest(PydanticBaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., min_length=3, max_length=50)
    category_id: int
    price: float


class ProductResponse(ProductRequest):
    id: Union[UUID, int, str]

    class Config:
        orm_mode = True
