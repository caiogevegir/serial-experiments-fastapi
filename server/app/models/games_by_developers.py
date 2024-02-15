from sqlalchemy import Column, Integer, ForeignKey

from config.database import Base

# ------------------------------------------------------------------------------


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
