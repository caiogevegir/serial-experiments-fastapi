from pydantic import BaseModel

# ------------------------------------------------------------------------------

class DevelopersBaseSchema(BaseModel):
  name: str
  country_code: str


class DevelopersCreateSchema(DevelopersBaseSchema):
  pass


class DevelopersSchema(DevelopersBaseSchema):
  id: int

  class Config:
    orm_mode = True
