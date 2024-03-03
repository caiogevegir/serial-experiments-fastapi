from pydantic import BaseModel

# ------------------------------------------------------------------------------

class PlatformsBaseSchema(BaseModel):
  name: str
  manufacturer: str


class PlatformsCreateSchema(PlatformsBaseSchema):
  pass


class PlatformsSchema(PlatformsBaseSchema):
  id: int

  class Config:
    from_attributes = True
