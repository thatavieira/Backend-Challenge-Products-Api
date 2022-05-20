from sqlalchemy import Column, Integer, String
from db import Base

class Challenge(Base):
    __tablename__ = "challenge"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(20))
    product = Column(String(20))
    