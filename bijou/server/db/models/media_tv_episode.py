from sqlalchemy import Column, ForeignKey, ForeignKeyConstraint, Integer, String
from .base import Base

class MediaTvEpisode(Base):
    __tablename__ = 'media_tv_episodes'
    id = Column(Integer, primary_key=True)
    file = Column(Integer, ForeignKey('media_files.id'), nullable=True)
    title = Column(String)

