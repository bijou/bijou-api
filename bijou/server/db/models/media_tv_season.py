from sqlalchemy import Column, ForeignKey, UniqueConstraint, Integer, String
from .base import Base

class MediaTVSeason(Base):
    __tablename__ = 'media_tv_seasons'
    tv_show = Column(Integer, ForeignKey('media_tv_shows.id'), primary_key=True)
    number = Column(Integer, primary_key=True)
    path = Column(String)
    __table_args__ = (
        UniqueConstraint('tv_show', 'number'),
    )
