from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, field_validator

from database import DB_ERROR_KEY
from sql import platforms as sql

router = APIRouter()

ENDPOINT = 'platforms'

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

@router.get(f'/{ENDPOINT}/list')
def list_platforms() -> list[dict] | dict:
  ret, err = sql.list_platforms()

  if err != None:
    raise HTTPException(status_code=500, detail=err)

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

@router.post(f'/{ENDPOINT}/add')
def add_platform(new_platform: Platform) -> dict:
  ret, err = sql.add_platform(
    new_platform.name,
    new_platform.manufacturer,
    new_platform.release_year
  )

  if err != None:
    raise HTTPException(status_code=500, detail=err)

  return {
    'name': new_platform.name,
    'manufacturer': new_platform.manufacturer,
    'release_year': new_platform.release_year
  }
