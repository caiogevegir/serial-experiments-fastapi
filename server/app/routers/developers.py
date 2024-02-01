from fastapi import APIRouter
from pydantic import BaseModel

from sql import developers as sql

router = APIRouter()

# GET --------------------------------------------------------------------------

@router.get('/developers/list')
def list_developers():
  pass

# POST -------------------------------------------------------------------------

@router.post('/developers/add')
def add_developer():
  pass