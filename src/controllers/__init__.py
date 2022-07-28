from fastapi import APIRouter
from src.repositories import repositories


def init_controller(name):
    router = APIRouter()
    repository = repositories[name]
    return router, repository
