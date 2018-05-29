# sqlalchemy configuration start same for every app

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


# configuration complete the above code is bascially required for every sqlalchemy app

class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True)
    link = Column(String(500))
    post = Column(String(100), nullable=False)


class Tender(Base):
    __tablename__ = "tender"
    id = Column(Integer, primary_key=True)
    link = Column(String(500))
    post = Column(String(100), nullable=False)


class Headlines(Base):
    __tablename__ = "headlines"
    id = Column(Integer, primary_key=True)
    link = Column(String(500))
    post = Column(String(100), nullable=False)


# initialize database and table

engine = create_engine('sqlite:///semari.db')

Base.metadata.create_all(engine)
