import re
import uuid
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, field_validator

from database import DB_ERROR_KEY
from sql import games as sql

router = APIRouter()

ENDPOINT = 'games'

#==============================================================================#
# MODELS                                                                       #
#==============================================================================#

class Game(BaseModel):
  name: str
  platform_id: int
  gameplay_status: str
  is_owned: bool
  commentary: str | None
  backlog_date: str
  start_date: str | None
  finish_date: str | None
  score: int | None

  @field_validator('name')
  def check_name(cls, value: str) -> str:
    if len(value) > 60:
      raise ValueError('length cannot be longer than 60.')
    return value

  @field_validator('gameplay_status')
  def check_gameplay_status(cls, value: str) -> str:
    valid_values = [ 
      'BACKLOG', 'PLAYING', 'HIATUS', 'FINISHED', 'CONTINUOUS', 'DROPPED'
    ]
    if value not in valid_values:
      raise ValueError(f'must be {valid_values}')
    return value
  
  @field_validator('commentary')
  def check_commentary(cls, value: str) -> str:
    if value != None and len(value) > 255:
      raise ValueError('length cannot be longer than 255.')
    return value
  
  @field_validator('backlog_date')
  def check_backlog_date(cls, value: str) -> str:
    if re.match(r'^\d{4}-[0-1]\d-[0-3]\d$', value) == None:
      raise ValueError('must be in format YYYY-MM-DD')
    return value
  
  @field_validator('start_date')
  def check_start_date(cls, value: str) -> str:
    if value != None and re.match(r'^\d{4}-[0-1]\d-[0-3]\d$', value) == None:
      raise ValueError('must be in format YYYY-MM-DD')
    return value

  @field_validator('finish_date')
  def check_finish_date(cls, value: str) -> str:
    if value != None and re.match(r'^\d{4}-[0-1]\d-[0-3]\d$', value) == None:
      raise ValueError('must be in format YYYY-MM-DD')
    return value

  @field_validator('score')
  def check_score(cls, value: int) -> int:
    if value != None and ( value < 0 or value > 10 ):
      raise ValueError('must be between 0 and 10.')
    return value

#==============================================================================#
# GET                                                                          #
#==============================================================================#

@router.get(f'/{ENDPOINT}/list')
def list_games(
  platform_id: int = None, 
  developer_id: int = None, 
  gameplay_status: str = None
):
  ret, err = sql.list_games(platform_id, developer_id, gameplay_status)
  
  if err != None:
    raise HTTPException(status_code=500, detail=err)

  return [
    {
      'id': id,
      'name': name,
      'platform': platform,
      'gameplay_status': gameplay_status,
      'score': score
    }
    for ( id, name, platform, gameplay_status, score ) in ret
  ]

# ------------------------------------------------------------------------------

@router.get(f'/{ENDPOINT}/detail')
def detail_game(id: str):
  ret, err = sql.detail_game(id)

  if err != None:
    raise HTTPException(status_code=500, detail=err)
  
  return [
    {
      'id': game_id,
      'name': name,
      'platform': platform,
      'gameplay_status': gameplay_status,
      'developers': developers,
      'is_owned':  is_owned,
      'commentary': commentary,
      'backlog_date': backlog_date,
      'start_date': start_date,
      'finish_date': finish_date,
      'score': score
    }
    for ( 
      game_id, name, platform, gameplay_status, developers, is_owned,
      commentary, backlog_date, start_date, finish_date, score
    ) in ret
  ]

#==============================================================================#
# POST                                                                         #
#==============================================================================#

@router.post(f'/{ENDPOINT}/add')
def add_game(new_game: Game):
  game_id = str(uuid.uuid4())

  ret, err = sql.add_game(
    game_id,
    new_game.name,
    new_game.platform_id,
    new_game.gameplay_status,
    new_game.is_owned,
    new_game.backlog_date,
    new_game.commentary,
    new_game.start_date,
    new_game.finish_date,
    new_game.score
  )

  if err != None:
    raise HTTPException(status_code=500, detail=err)

  return {
    'id': game_id
  }

# ------------------------------------------------------------------------------

@router.post(f'/{ENDPOINT}/assign-developers')
def assign_game_to_developers(game_id: str, developers_id: list[int]):
  ret, err = sql.assign_game_to_developers(game_id, developers_id)

  if err != None:
    raise HTTPException(status_code=500, detail=err)

  return {
    'id': game_id
  }

#==============================================================================#
# PUT                                                                          #
#==============================================================================#

@router.put(f'/{ENDPOINT}/update')
def update_game(game_id: str, updated_game: Game):
  ret, err = sql.quick_search_game(game_id)

  if err != None:
    raise HTTPException(status_code=500, detail=err)
  if ret == []:
    raise HTTPException(status_code=404, detail='Game not found')
  
  ret, err = sql.update_game(
    game_id,
    updated_game.name,
    updated_game.platform_id,
    updated_game.gameplay_status,
    updated_game.is_owned,
    updated_game.backlog_date,
    updated_game.commentary,
    updated_game.start_date,
    updated_game.finish_date,
    updated_game.score
  )

  if err != None:
    raise HTTPException(status_code=500, detail=err)

  return {
    'id': game_id,
    'name': updated_game.name,
    'platform_id': updated_game.platform_id,
    'gameplay_status': updated_game.gameplay_status,
    'is_owned': updated_game.is_owned,
    'commentary': updated_game.commentary,
    'backlog_date': updated_game.backlog_date,
    'start_date': updated_game.start_date,
    'finish_date': updated_game.finish_date,
    'score': updated_game.score
  }
  
#==============================================================================#
# DELETE                                                                       #
#==============================================================================#

@router.delete(f'/{ENDPOINT}/unassign-developer')
def unassign_game_from_developer(game_id: str, developer_id: int):
  ret, err = sql.unassign_game_from_developer(game_id, developer_id)

  if err != None:
    raise HTTPException(status_code=500, detail=err)

  return {
    'game_id': game_id,
    'developer_id': developer_id
  }

# ------------------------------------------------------------------------------

@router.delete(f'/{ENDPOINT}/remove')
def remove_game(game_id: str):
  ret, err = sql.delete_game(game_id)
  
  if err != None:
    raise HTTPException(status_code=500, detail=err)

  return {
    'game_id': game_id
  }
