from .main import AppService, ServiceResult

from repositories.developers import DevelopersCRUD
from schemas.developers import DevelopersCreateSchema
from errors.developers import DevelopersException

# ------------------------------------------------------------------------------

class DevelopersService(AppService):

  def list_developers(self) -> ServiceResult:
    developers = DevelopersCRUD(self.db).list_developers()
    if developers == None:
      return ServiceResult(DevelopersException.UnableToListDevelopers())
    return ServiceResult(developers)
    
  def add_developer(
    self, 
    developer: DevelopersCreateSchema
  ) -> ServiceResult:
    new_developer = DevelopersCRUD(self.db).add_developer(developer)
    if new_developer == None:
      return ServiceResult(DevelopersException.UnableToAddDevelopers())
    return ServiceResult(new_developer)
