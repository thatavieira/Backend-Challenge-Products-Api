from sqlalchemy import Column, Integer, String
from app.database import Base

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    description = Column(String(20))
    price = Column(Integer)


