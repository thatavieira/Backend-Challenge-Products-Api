import app.models.product_model as model_product
import app.models.category_model as model_category
from app.database import engine


model_product.Base.metadata.create_all(bind=engine)
model_category.Base.metadata.create_all(bind=engine)
