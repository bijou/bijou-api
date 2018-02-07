from sqlalchemy import Column, Integer, String
from .base import Base

class MediaFile(Base):
    __tablename__ = 'media_files'
    id = Column(Integer, primary_key=True)
    path = Column(String)
