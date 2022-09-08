from sqlalchemy import Boolean, Column, Float, Integer, String

from app.database import Base


class Item(Base):
    boolean = Column(Boolean())
    floating = Column(Float())
    integer = Column(Integer())
    string = Column(String(120))
