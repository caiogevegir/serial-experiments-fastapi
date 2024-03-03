from .main import AppCRUD
from models.platforms import PlatformsModel
from schemas.platforms import PlatformsCreateSchema

# ------------------------------------------------------------------------------

class PlatformsCRUD(AppCRUD):

  def list_platforms(self) -> list[PlatformsModel] | None:
    try:
      return self.db.query(PlatformsModel).all()
    except:
      return None
  
  def add_platform(
    self, 
    platform: PlatformsCreateSchema
  ) -> PlatformsModel | None:
    try:
      new_platform = PlatformsModel(**platform.model_dump())
      self.db.add(new_platform)
      self.db.commit()
      self.db.refresh(new_platform)
      return new_platform
    except:
      return None
