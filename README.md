<h3 align="center">Product API</h3>
<p align="center">
<a href="https://github.com/thatavieira/backend_challenge_products_api"><img alt="products_api" src="https://img.shields.io/badge/products__api-1.2.1-orange" /></a>
<a href="https://pypi.org/"><img alt="fastApi" src="https://img.shields.io/badge/fastApi-0.75.1-green"/></a>
<a href="https://pypi.org/"><img alt="uvicorn" src="https://img.shields.io/badge/uvicorn-0.17.6-red"/></a>
<a href="https://pypi.org/"><img alt="SQLAchemy" src="https://img.shields.io/badge/SQLAchemy-1.4.36-9cf"/></a>
<a href="https://pypi.org/"><img alt="psycopg2-binary" src="https://img.shields.io/badge/psycopg2--binary-2.9.3-yellow"/></a>
<a href="https://pypi.org/"><img alt="fastApi-pagination" src="https://img.shields.io/badge/fastApi--pagination-0.9.3-blue"/></a>
<a href="https://pypi.org/"><img alt="pydantic" src="https://img.shields.io/badge/pydantic-1.9.1-inactive"/></a></p>

<p align="center">
<img alt="logo" src="https://raw.githubusercontent.com/thatavieira/backend_challenge_products_api/developer/img/fast_api.png"/>
</p>


# About The Project

Project created for realize Challenge Backend Products Api, project which allows manipulate and relate products and categories.

* Mandatory requirements
    
    1.User should be able of create, read, update and delete products.
    
    2.User should be able of create, read, update and delete categories.

    3.A product must be related to a category.

    4.A category must be related to one or more products.

    5.Queries must return a maximum of 10 items by request.

    6.The product query should be able to return a specific product or all of them.

    7.The category query must be able to return a specific category or all.


Product output:
```
[
    {
        "id": 1,
        "name": "Nike Shoes for Man",
        "description": "Nike Shoes",
        "price": 199.99,
        "category": {
            "id": 1,
            "name": "Shoes"
        }
    },
    {
        "id": 2,
        "name": "Amanda Waller Shirt Men",
        "description": "New awesome shirt",
        "price": 32.49,
        "category": {
            "id": 2,
            "name": "Shirts"
        }
    }
]
```


Category output:
```    
[
    {
        "id": 1,
        "name": "Shoes"
    },
    {
        "id": 2,
        "name": "Shirts"
    }
]
```



# Build With

Follow list with any frameworks and libs used in building of the application.

* FastApi
* Uvicorn
* SQLAlchemy
* Psycopg2-Binary
* FastApi-Pagination
* Pydantic

# Getting Started

To build and run the application, you need to install the dependencies below:

* Steps for configuration

1. Clone application
    
    ```
    git clone https://git@github.com/thatavieira/backend_challenge_products_api.git
    ```
    
2. Creating and Initializing Virtual Enviroment

    ```
    python3 -m venv .venv && source venv/bin/activate
    ```
3. Installing Packages

    ```
    python3 -m pip install -r requirements.txt
    ```

4. Initializing API

    ```
    python3 main.py  
    ```
Ps.: You must have PostgreSQL installed, if not you can use Docker as below.

* Docker - Optional

1. If you want to run the application in docker, configure the file docker-compose and after the command 
```
docker-compose up --build -d
```

2.Configure the environment variables for containers in `docker-compose.yml` file:

#### docker-compose.yml
```
version: "3.7"

services:
  app:
    build: .
    container_name: app
    command:  uvicorn src.api:app --host 0.0.0.0
    ports:
      - 8000:8000
    depends_on:
      - "db"

  db:
    image: postgres:12.1-alpine
    container_name: db
    ports:
      - 5432:5432
    environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
```

# Development

API developed with FastApi, framework focused on API development, modern, fast, simple and robust. Using Uvicorn to implement web server.
FastApi-Pagination used to limit the amount of information for each request, so avoiding data overload for query.
SQLAlchemy an ORM created with Python which can access a database using Python instead of SQL.
Pyscopg2 used to connect to PostgreSQL database.
Pydantic a library that analyzes and validates data returning easy-to-understand answers.



# Contribuiting
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply opena an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

