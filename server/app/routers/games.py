from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.database import get_db
from services.games import GamesService
from schemas.games import GamesSchema, GamesCreateSchema, GamesUpdateSchema, \
  GamesAssignToDeveloperSchema

router = APIRouter(prefix='/games')

# GET --------------------------------------------------------------------------

@router.get('', response_model=list[GamesSchema])
async def list_games(
  id: int = None,
  status: str = None,
  ownership: str = None,
  platform_id: int = None,
  db: Session = Depends(get_db)
):
  filters = {}
  if id:
    filters['id'] = id
  if status:
    filters['status'] = status
  if ownership:
    filters['ownership'] = ownership
  if platform_id:
    filters['platform_id'] = platform_id
  
  return GamesService(db).list_games(filters).handle_result()

# POST -------------------------------------------------------------------------

@router.post('', response_model=GamesSchema)
async def add_game(new_game: GamesCreateSchema, db: Session = Depends(get_db)):
  return GamesService(db).add_game(new_game).handle_result()

@router.post('/developers', response_model=GamesAssignToDeveloperSchema)
async def assign_to_developer(
  payload: GamesAssignToDeveloperSchema,
  db: Session = Depends(get_db)
):
  return GamesService(db).assign_developers(payload).handle_result()

# PUT --------------------------------------------------------------------------

@router.put('', response_model=GamesUpdateSchema)
async def update_game(
  updated_game: GamesUpdateSchema,
  db: Session = Depends(get_db)
):
  return GamesService(db).update_game(updated_game).handle_result()

# DELETE -----------------------------------------------------------------------

@router.delete('', response_model=dict)
async def remove_game(id: str, db: Session = Depends(get_db)):
  return GamesService(db).remove_game(int(id)).handle_result()
