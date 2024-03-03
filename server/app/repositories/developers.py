from .main import AppCRUD

from models.developers import DevelopersModel
from schemas.developers import DevelopersCreateSchema

# ------------------------------------------------------------------------------

class DevelopersCRUD(AppCRUD):

  def list_developers(self) -> list[DevelopersModel] | None:
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