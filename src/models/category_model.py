from uuid import UUID
from typing import Union
from src.database import Base
from sqlalchemy import Column, String
from src.models.base_model import BaseModel
from pydantic import Field, BaseModel as PydanticBaseModel


class Category(BaseModel, Base):
    __tablename__ = 'categories'

    name = Column(String(50), nullable=False, index=True, unique=True)


class CategoryRequest(PydanticBaseModel):
    name: str = Field(..., min_length=3, max_length=50)


class CategoryResponse(CategoryRequest):
    id: Union[UUID, int, str]

    class Config:
        orm_mode = True

