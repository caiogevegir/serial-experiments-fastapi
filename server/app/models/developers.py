from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base
from .games_by_developers import games_by_developers

# ------------------------------------------------------------------------------

class DevelopersModel(Base):
  __tablename__ = 'developers'

  id = Column(
    'id', 
    Integer, 
    primary_key=True,
    autoincrement='auto'
  )

  name = Column(
    'name',
    String(30),
    unique=True,
    nullable=False
  )

  country_code = Column(
    'country_code',
    String(2),
    nullable=False
  )

  games = relationship(
    'GamesModel',
    secondary=games_by_developers,
    back_populates='developers'
  )
