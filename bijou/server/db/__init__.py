import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .models import *
from .models.base import Base

Session = sessionmaker()

def init_db(db):
    logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)
    engine = create_engine(db)
    Base.metadata.create_all(engine)
    Session.configure(bind=engine)
