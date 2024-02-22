from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.database import get_db
from services.games import GamesService
from schemas.games import GamesSchema, GamesCreateSchema, GamesUpdateSchema

router = APIRouter(prefix='/games')

# GET --------------------------------------------------------------------------

@router.get('/list', response_model=list[GamesSchema])
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

@router.post('/add', response_model=GamesSchema)
async def add_game(new_game: GamesCreateSchema, db: Session = Depends(get_db)):
  return GamesService(db).add_game(new_game).handle_result()

# PUT --------------------------------------------------------------------------

@router.put('/update/{game_id}', response_model=GamesSchema)
async def update_game(
  game_id: int,
  updated_game: GamesUpdateSchema,
  db: Session = Depends(get_db)
):
  params = {}
  if updated_game.status:
    params['status'] = updated_game.status
  if updated_game.ownership:
    params['ownership'] = updated_game.ownership
  if updated_game.platform_id:
    params['platform_id'] = updated_game.platform_id
  if updated_game.finish_date:
    params['finish_date'] = updated_game.finish_date
  if updated_game.score:
    params['score'] = updated_game.score

  return GamesService(db).update_game(game_id, params).handle_result()

# DELETE -----------------------------------------------------------------------

@router.delete('/remove{game_id}', response_model=int)
async def remove_game(game_id: int, db: Session = Depends(get_db)):
  return GamesService(db).remove_game(game_id).handle_result()
