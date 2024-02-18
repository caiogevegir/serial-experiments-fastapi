from main import AppService, AppCRUD, ServiceResult
from models.developers import DevelopersModel
from schemas.developers import DevelopersCreateSchema
from errors.developers import DevelopersException

# ------------------------------------------------------------------------------

class DevelopersService(AppService):

  def list_all_developers(self) -> ServiceResult:
    developers = DevelopersCRUD(self.db).list_all_developers()
    if developers == None:
      return ServiceResult(DevelopersException.FailedToListDevelopers())
    return ServiceResult(developers)
    
  def add_developer(
    self, 
    developer: DevelopersCreateSchema
  ) -> ServiceResult:
    new_developer = DevelopersCRUD(self.db).add_developer(developer)
    if new_developer == None:
      return ServiceResult(DevelopersException.FailedToAddDevelopers())
    return ServiceResult(new_developer)
    

# ------------------------------------------------------------------------------

class DevelopersCRUD(AppCRUD):

  def list_all_developers(self) -> list[DevelopersModel] | None:
    try:
      return self.db.query(DevelopersModel).all()
    except:
      return None

  def add_developer(
    self,
    developer: DevelopersCreateSchema
  ) -> DevelopersModel | None:
    try:
      new_developer = DevelopersModel(**developer.model_dump())
      self.db.add(new_developer)
      self.db.commit()
      self.db.refresh(new_developer)
      return new_developer
    except:
      return None