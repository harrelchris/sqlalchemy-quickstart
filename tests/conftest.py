import os

import pytest
from sqlalchemy import Boolean, Column, Float, Integer, String

os.environ.setdefault('DATABASE_URL', "sqlite:///:memory:")

from app.database import Base


class Thing(Base):
    boolean = Column(Boolean())
    floating = Column(Float())
    integer = Column(Integer())
    string = Column(String(120))


@pytest.fixture
def model():
    return Thing(
        boolean=True,
        floating=3.14,
        integer=42,
        string="value",
    )
