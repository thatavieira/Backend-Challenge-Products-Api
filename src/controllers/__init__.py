from src.models.product_model import ProductRequest, ProductResponse
from src.models.category_model import Category, CategoryRequest, CategoryResponse

from src.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List
from fastapi import APIRouter
from src.repositories import repositories


def init_controller(name):
    router = APIRouter()
    repository = repositories[name]
    return router, repository

