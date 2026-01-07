from sqlalchemy import Column, Integer, String, Text
from app.models.base import Base

class Item(Base):
    tablename = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    description = Column(Text, nullable=True)
    owner_name = Column(String(50), nullable=True)