from .main import AppService, ServiceResult

from repositories.platforms import PlatformsCRUD
from schemas.platforms import PlatformsCreateSchema
from errors.platforms import PlatformsException

# ------------------------------------------------------------------------------

class PlatformsService(AppService):

  def list_platforms(self) -> ServiceResult:
    platforms = PlatformsCRUD(self.db).list_platforms()
    if platforms == None:
      return ServiceResult(PlatformsException.UnableToListPlatforms())
    return ServiceResult(platforms)
  
  def add_platform(self, platform: PlatformsCreateSchema) -> ServiceResult:
    new_platform = PlatformsCRUD(self.db).add_platform(platform)
    if new_platform == None:
      return ServiceResult(PlatformsException.UnableToAddPlatform())
    return ServiceResult(new_platform)
