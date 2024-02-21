from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.database import get_db
from services.developers import DevelopersService
from schemas.developers import DevelopersSchema, DevelopersCreateSchema

router = APIRouter(prefix='/developers')

# GET --------------------------------------------------------------------------

@router.get('/list', response_model=list[DevelopersSchema])
async def list_all_developers(db: Session = Depends(get_db)):
  return DevelopersService(db).list_all_developers().handle_result()

# POST -------------------------------------------------------------------------

@router.post('/add', response_model=DevelopersSchema)
async def add_developer(
  new_developer: DevelopersCreateSchema,
  db: Session = Depends(get_db)
):
  return DevelopersService(db).add_developer(new_developer).handle_result()
