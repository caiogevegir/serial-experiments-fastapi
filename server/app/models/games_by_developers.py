from enum import Enum
from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from config.database import Base


class GamesByDevelopersModel(Base):
  __tablename__ = 'games_by_developers'

  game_id = Column(
    'game_id',
    Integer,
    ForeignKey('games.id', ondelete='CASCADE'),
    primary_key=True
  )

  developer_id = Column(
    'developer_id',
    Integer,
    ForeignKey('developers.id', ondelete='CASCADE'),
    primary_key=True
  )
