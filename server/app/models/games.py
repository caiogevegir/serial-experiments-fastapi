from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum
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

  backlog_date = Column(
    'backlog_date',
    Date,
    nullable=False
  )

  finish_date = Column(
    'finish_date',
    Date
  )

  score = Column(
    'score',
    Integer
  )

  platform = relationship(
    'PlatformsModel',
    back_populates='games'
  )

  developers = relationship(
    'DevelopersModel',
    secondary=games_by_developers,
    back_populates='games'
  )
