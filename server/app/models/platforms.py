from enum import Enum
from sqlalchemy import Column, Boolean, Integer, String, ForeignKeyConstraint, Date
from sqlalchemy.orm import relationship

from config.database import Base


class PlatformsModel(Base):
  __tablename__ = 'platforms'

  id = Column(
    'id', 
    Integer, 
    primary_key=True,
    autoincrement='auto'
  )

  name = Column(
    'name',
    String(20),
    unique=True,
    nullable=False
  )

  games = relationship(
    'GamesModel',
    back_populates='platform'
  )

  manufacturer = Column(
    'manufacturer',
    String(20),
    nullable=False
  )

  release_year = Column(
    'manufacturer',
    Integer,
    nullable=False
  )