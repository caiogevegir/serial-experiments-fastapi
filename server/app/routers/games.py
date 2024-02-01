from fastapi import APIRouter
from pydantic import BaseModel

from sql import games as sql

router = APIRouter()

# GET --------------------------------------------------------------------------

@router.get('/games/list')
def list_games():
  pass


# POST -------------------------------------------------------------------------

@router.post('/games/add')
def add_game():
  pass

# PUT --------------------------------------------------------------------------

@router.put('/games/update')
def update_game():
  pass

# DELETE -----------------------------------------------------------------------

@router.delete('/games/remove')
def remove_game():
  pass