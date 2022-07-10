from app.models.product_model import ProductRequest, ProductResponse
from app.models.category_model import Category, CategoryRequest, CategoryResponse

from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List
from fastapi import APIRouter
from app.repositories import repositories


def init_controller(name):
    router = APIRouter()
    repository = repositories[name]
    return router, repository

