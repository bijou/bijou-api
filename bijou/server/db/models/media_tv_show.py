from sqlalchemy import Column, UniqueConstraint, Integer, String
from .base import Base

class MediaTVShow(Base):
    __tablename__ = 'media_tv_shows'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    path = Column(String)
    __table_args__ = (
        UniqueConstraint('name'),
    )
