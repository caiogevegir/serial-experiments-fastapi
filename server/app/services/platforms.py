from .main import AppService, AppCRUD, ServiceResult
from models.platforms import PlatformsModel
from schemas.platforms import PlatformsCreateSchema
from errors.platforms import PlatformsException

# ------------------------------------------------------------------------------

class PlatformsService(AppService):

  def list_platforms(self) -> ServiceResult:
    platforms = PlatformsCRUD(self.db).list_all_platforms()
    if platforms == None:
      return ServiceResult(PlatformsException.UnableToListPlatforms())
    return ServiceResult(platforms)
  
  def add_platform(self, platform: PlatformsCreateSchema) -> ServiceResult:
    new_platform = PlatformsCRUD(self.db).add_platform(platform)
    if new_platform == None:
      return ServiceResult(PlatformsException.UnableToAddPlatform())
    return ServiceResult(new_platform)
    

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
