import re
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, field_validator

from database import DB_ERROR_KEY
from sql import developers as sql

router = APIRouter()

ENDPOINT = 'developers'

#==============================================================================#
# MODELS                                                                       #
#==============================================================================#

class Developer(BaseModel):
  name: str
  country_code: str

  @field_validator('name')
  def check_name(cls, value: str) -> str:
    if len(value) > 50:
      raise ValueError('length cannot be longer than 50.')
    return value
  
  @field_validator('country_code')
  def check_country_code(cls, value: str) -> str:
    if len(value) > 2:
      raise ValueError('length cannot be longer than 2.')
    return value

#==============================================================================#
# GET                                                                          #
#==============================================================================#

@router.get(f'/{ENDPOINT}/list')
def list_developers():
  ret, err = sql.list_developers()

  if err != None:
    raise HTTPException(status_code=500, detail=err)

  return [
    {
      'id': id,
      'name': name,
      'country_code': country_code
    }
    for ( id, name, country_code ) in ret
  ]

#==============================================================================#
# POST                                                                         #
#==============================================================================#

@router.post(f'/{ENDPOINT}/add')
def add_developer(new_developer: Developer):
  ret, err = sql.add_developer(
    new_developer.name,
    new_developer.country_code,
  )

  if err != None:
    raise HTTPException(status_code=500, detail=err)

  return {
    'name': new_developer.name,
    'manufacturer': new_developer.country_code,
  }
