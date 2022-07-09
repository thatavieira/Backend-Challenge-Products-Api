from uuid import UUID
from typing import Union
from app.database import Base
from sqlalchemy import Column, Integer, String
from app.models.base_model import BaseModel
from pydantic import Field, BaseModel as PydanticBaseModel


class Category(BaseModel, Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name_category = Column(String(20))


class CategoryRequest(PydanticBaseModel):
    description: str = Field(..., min_length=3, max_length=20)


class CategoryResponse(CategoryRequest):
    id: Union[UUID, int, str]
