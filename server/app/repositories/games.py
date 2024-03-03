from .main import AppCRUD

from models.games import GamesModel
from models.developers import DevelopersModel
from schemas.games import GamesCreateSchema, GamesUpdateSchema, \
  GamesAssignToDeveloperSchema

# ------------------------------------------------------------------------------

class GamesCRUD(AppCRUD):

  def list_games(self, filters: dict) -> list[GamesModel] | None:
    try:
      return self.db.query(GamesModel).filter_by(**filters).all()
    except:
      return None   
 
  def add_game(self, game: GamesCreateSchema) -> GamesModel | None:
    try:
      new_game = GamesModel(**game.model_dump())
      self.db.add(new_game)
      self.db.commit()
      self.db.refresh(new_game)
      return new_game
    except:
      return None
  
  def assign_developers(self, game_id: int, developers_id: list[int]):
    try:
      game = self.db.query(GamesModel).get(game_id)
      # TODO: Is there a more efficient way to do this?
      for developer_id in developers_id:
        developer = self.db.query(DevelopersModel).get(developer_id)
        game.developers.append(developer)
      self.db.commit()
      return True
    except:
      return None
  
  def update_game(self, updated_game: GamesUpdateSchema) -> int | None:
    try:
      rows = self.db.query(GamesModel).filter_by(id=updated_game.id).update({
        'status': updated_game.status,
        'score': updated_game.score
      })
      self.db.commit()
      return rows
    except:
      return None
  
  def remove_game(self, id: int) -> int | None:
    try:
      rows = self.db.query(GamesModel).filter(GamesModel.id == id).delete(
        synchronize_session=False
      )
      self.db.commit()
      return rows
    except:
      return None