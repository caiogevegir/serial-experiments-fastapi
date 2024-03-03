from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship

from config.database import Base
from utils.enums import GameStatus, OwnershipStatus
from .games_by_developers import games_by_developers

# ------------------------------------------------------------------------------

class GamesModel(Base):
  __tablename__ = 'games'

  id = Column(
    'id',
    Integer,
    primary_key=True,
    autoincrement='auto'
  )

  name = Column(
    'name',
    String(64),
    unique=True,
    nullable=False
  )

  platform_id = Column(
    'platform_id',
    Integer,
    ForeignKey('platforms.id'),
    nullable=False
  )

  status = Column(
    'status',
    Enum(GameStatus),
    nullable=False
  )

  ownership = Column(
    'ownership',
    Enum(OwnershipStatus),
    nullable=False
  )

  score = Column(
    'score',
    Integer
  )

  platform = relationship(
    'PlatformsModel'
  )

  developers = relationship(
    'DevelopersModel',
    secondary=games_by_developers
  )
