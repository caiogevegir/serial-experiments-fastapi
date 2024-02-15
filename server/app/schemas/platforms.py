from pydantic import BaseModel

# ------------------------------------------------------------------------------

class PlatformsBaseSchema(BaseModel):
  name: str
  manufacturer: str
  release_year: int


class PlatformsCreateSchema(PlatformsBaseSchema):
  pass


class PlatformsSchema(PlatformsBaseSchema):
  id: str
  games: list[str] = []

  class Config:
    orm_mode = True
