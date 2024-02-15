from pydantic import BaseModel

from utils.enums import GameStatus, OwnershipStatus

# ------------------------------------------------------------------------------

class GamesBaseSchema(BaseModel):
  name: str
  status: GameStatus
  ownership: OwnershipStatus
  backlog_date: str
  finish_date: str
  score: int


class GamesCreateSchema(GamesBaseSchema):
  platform_id: int
  developers_id: list[int]


class GamesUpdateSchema(GamesCreateSchema):
  pass


class GamesSchema(GamesBaseSchema):
  id: int
  platform: str
  developers: list[str]

  class Config:
    orm_mode = True
