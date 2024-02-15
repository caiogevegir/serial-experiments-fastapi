from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from config.database import Base
from utils.enums import GameStatus, OwnershipStatus

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

  platform = relationship(
    'PlatformsModel',
    back_populates='games'
  )

  developers = relationship(
    secondary='GamesByDevelopersModel',
    back_populates='games'
  )

  status = Column(
    'status',
    GameStatus,
    nullable=False
  )

  ownership = Column(
    'ownership',
    OwnershipStatus,
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
