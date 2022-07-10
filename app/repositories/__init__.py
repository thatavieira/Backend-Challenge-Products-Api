import app.models.product_model as model_product
import app.models.category_model as model_category
from app.database import engine
from . import product_repository
from . import category_repository


model_product.Base.metadata.create_all(bind=engine)
model_category.Base.metadata.create_all(bind=engine)

repositories = \
    {
        "product": product_repository,
        "category": category_repository,
    }

