from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.database import get_db
from services.platforms import PlatformsService
from schemas.platforms import PlatformsSchema, PlatformsCreateSchema

router = APIRouter(prefix='/platforms')

# GET --------------------------------------------------------------------------
  
@router.get('', response_model=list[PlatformsSchema])
async def list_all_platforms(db: Session = Depends(get_db)):
  return PlatformsService(db).list_platforms().handle_result()

# POST -------------------------------------------------------------------------

@router.post('', response_model=PlatformsSchema)
async def add_platform(
  new_platform: PlatformsCreateSchema, 
  db: Session = Depends(get_db)
):
  return PlatformsService(db).add_platform(new_platform).handle_result()

