from uuid import UUID
from typing import Union
from app.database import Base
from sqlalchemy import Column, Integer, String, Float
from app.models.base_model import BaseModel
from pydantic import Field, BaseModel as PydanticBaseModel


class Product(BaseModel, Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    description = Column(String(20))
    price = Column(Float)


class ProductRequest(PydanticBaseModel):
    name: str = Field(..., min_length=3, max_length=20)
    description: str = Field(..., min_length=3, max_length=20)
    price: float


class ProductResponse(ProductRequest):
    id: Union[UUID, int, str]

