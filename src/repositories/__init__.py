import importlib

import src.models.category_model as model_category
import src.models.product_model as model_product
from src.db import engine

model_product.Base.metadata.create_all(bind=engine)
model_category.Base.metadata.create_all(bind=engine)

repositories = {
    "product": importlib.import_module("src.repositories.product_repository"),
    "category": importlib.import_module("src.repositories.category_repository"),
}
