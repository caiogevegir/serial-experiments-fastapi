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


class GamesUpdateSchema(BaseModel):
  status: GameStatus | None
  ownership: OwnershipStatus | None
  platform_id: int | None
  finish_date: str | None
  score: int | None


class GamesSchema(GamesBaseSchema):
  id: int
  platform: str
  developers: list[str]

  class Config:
    orm_mode = True
