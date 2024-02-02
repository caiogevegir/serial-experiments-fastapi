from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, field_validator

from database import DB_ERROR_KEY
from sql import platforms as sql

router = APIRouter()

# ------------------------------------------------------------------------------

class Platform(BaseModel):
  name: str
  manufacturer: str
  release_year: int

  @field_validator('name')
  def check_name(cls, value: str) -> str:
    if len(value) > 50:
      raise ValueError('length cannot be longer than 50.')
    return value
  
  @field_validator('manufacturer')
  def check_manufacturer(cls, value: str) -> str:
    if len(value) > 50:
      raise ValueError('length cannot be longer than 50.')
    return value

  @field_validator('release_year')
  def check_release_year(cls, value: int) -> int:
    if value < 1900 or value > 2999:
      raise ValueError('must be between 1900 and 2999.')
    return value

# GET --------------------------------------------------------------------------

@router.get('/platforms/list')
def list_platforms() -> list[dict] | dict:
  ret = sql.list_platforms()

  if isinstance(ret, dict) and DB_ERROR_KEY in ret.keys():
    raise HTTPException(status_code=500, detail=ret)

  return [
    {
      'id': id,
      'name': name,
      'manufacturer': manufacturer,
      'release_year': release_year
    }
    for ( id, name, manufacturer, release_year ) in ret
  ]


# POST -------------------------------------------------------------------------

@router.post('/platforms/add')
def add_platform(new_platform: Platform) -> dict:
  ret = sql.add_platform(
    new_platform.name,
    new_platform.manufacturer,
    new_platform.release_year
  )

  if isinstance(ret, dict) and DB_ERROR_KEY in ret.keys():
    raise HTTPException(status_code=500, detail=ret)

  return {
    'name': new_platform.name,
    'manufacturer': new_platform.manufacturer,
    'release_year': new_platform.release_year
  }
