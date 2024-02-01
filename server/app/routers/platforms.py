from fastapi import APIRouter
from pydantic import BaseModel

from sql import platforms as sql

router = APIRouter()

# GET --------------------------------------------------------------------------

@router.get('/platforms/list')
def list_platforms():
  pass

# POST -------------------------------------------------------------------------

@router.post('/platforms/add')
def add_platform():
  pass