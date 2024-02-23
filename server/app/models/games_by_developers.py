from sqlalchemy import Column, Integer, ForeignKey, Table

from config.database import Base

# ------------------------------------------------------------------------------

games_by_developers = Table(
  'games_by_developers',
  Base.metadata,
  Column(
    'game_id',
    Integer,
    ForeignKey('games.id', ondelete='CASCADE')
  ),
  Column(
    'developer_id',
    Integer,
    ForeignKey('developers.id', ondelete='CASCADE')
  )
)
