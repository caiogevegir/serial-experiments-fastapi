from pydantic import BaseModel

from .platforms import PlatformsBaseSchema
from .developers import DevelopersBaseSchema
from utils.enums import GameStatus, OwnershipStatus

# ------------------------------------------------------------------------------

class GamesBaseSchema(BaseModel):
  name: str
  status: GameStatus
  ownership: OwnershipStatus
  score: int


class GamesCreateSchema(GamesBaseSchema):
  platform_id: int


class GamesAssignToDeveloperSchema(BaseModel):
  game_id: int
  developers_id: list[int]


class GamesUpdateSchema(BaseModel):
  id: int
  status: GameStatus
  score: int


class GamesSchema(GamesBaseSchema):
  id: int
  platform: PlatformsBaseSchema
  developers: list[DevelopersBaseSchema]

  class Config:
    orm_mode = True
