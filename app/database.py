import os

from sqlalchemy import Column, DateTime, Integer, MetaData, create_engine, func
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker
from sqlalchemy_mixins import AllFeaturesMixin

engine = create_engine(os.environ["DATABASE_URL"], echo=False)
session = scoped_session(sessionmaker(bind=engine, autocommit=True))
metadata = MetaData()


class BaseModel(AllFeaturesMixin):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime(timezone=False), server_default=func.now())
    modified = Column(DateTime(timezone=False), onupdate=func.now())

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


BaseModel.set_session(session)
Base = declarative_base(metadata=metadata, cls=BaseModel)
