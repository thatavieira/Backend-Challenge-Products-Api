from uuid import UUID
from typing import Union, Optional
from src.db import Base
from sqlalchemy import Column, String, Float, ForeignKey, Integer
from src.models.base_model import BaseModel
from pydantic import Field, BaseModel as PydanticBaseModel
from .category_model import Category, CategoryResponse
from sqlalchemy.orm import relationship


class Product(BaseModel, Base):
    __tablename__ = 'products'

    def __init__(self, product):
        self.name = product.name
        self.description = product.description
        self.price = self.validate_price(product.price)
        self.category_id = product.category_id

    @staticmethod
    def validate_price(price):
        if price <= 0:
            raise Exception("Price must be greater than zero")

        return price

    name = Column(String(50), nullable=False, index=True, unique=True)
    description = Column(String(50), nullable=False)
    price = Column(Float)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship(Category, lazy='joined')


class ProductRequest(PydanticBaseModel):
    name: str = Field(..., min_length=3, max_length=50, exclude=False)
    description: str = Field(..., min_length=3, max_length=50, exclude=False)
    category_id: Optional[int] = None
    price: float


class ProductResponse(ProductRequest):
    id: Union[UUID, int, str]
    category: CategoryResponse

    class Config:
        orm_mode = True
        fields = {'category_id': {'exclude': True}}
