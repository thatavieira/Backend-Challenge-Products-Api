from app.controllers import category_controller as category
from app.controllers import product_controller as product
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Product Api",
        version="1.0.0",
        description="Backend challenge implementation Products Api",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


@app.on_event("startup")
async def init_conns():
    """Init external connections & middlewares
    All clients will be initialized once only as Singletons
    """


app.include_router(category.router, prefix="/categories", tags=["Category"])
app.include_router(product.router, prefix="/products", tags=["Product"])
#app.openapi = custom_openapi
