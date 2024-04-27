from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from database import Base

Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    is_offer = Column(String, nullable=True)
