from fastapi import APIRouter
from pydantic import BaseModel

from sql import games as sql

router = APIRouter()

ENDPOINT = 'games'

# GET --------------------------------------------------------------------------

@router.get(f'/{ENDPOINT}/list')
def list_games():
  pass


# POST -------------------------------------------------------------------------

@router.post(f'/{ENDPOINT}/add')
def add_game():
  pass

# PUT --------------------------------------------------------------------------

@router.put(f'/{ENDPOINT}/update')
def update_game():
  pass

# DELETE -----------------------------------------------------------------------

@router.delete(f'/{ENDPOINT}/remove')
def remove_game():
  pass