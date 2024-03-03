from .main import AppService, AppCRUD, ServiceResult
from models.games import GamesModel
from models.developers import DevelopersModel
from models.games_by_developers import games_by_developers
from schemas.games import GamesCreateSchema, GamesUpdateSchema, \
  GamesAssignToDeveloperSchema
from errors.games import GamesException

# ------------------------------------------------------------------------------

class GamesService(AppService):

  def list_games(self, filters: dict) -> ServiceResult:
    games = GamesCRUD(self.db).list_games(filters)
    if games == None:
      return ServiceResult(GamesException.UnableToListGames())
    return ServiceResult(games)

  def add_game(self, game: GamesCreateSchema) -> ServiceResult:
    new_game = GamesCRUD(self.db).add_game(game)
    if new_game == None:
      return ServiceResult(GamesException.UnableToCreateGame())
    return ServiceResult(new_game)
  
  def assign_developers(
    self,
    payload: GamesAssignToDeveloperSchema
  ) -> ServiceResult:
    ret = GamesCRUD(self.db).assign_developers(
      payload.game_id, 
      payload.developers_id
    )
    if ret == None:
      return ServiceResult(GamesException.UnableToAssignDevelopersToGame())
    return ServiceResult(payload)
  
  def update_game(self, updated_game: GamesUpdateSchema) -> ServiceResult:
    rows = GamesCRUD(self.db).update_game(updated_game)
    if rows == None:
      return ServiceResult(GamesException.UnableToUpdateGame())
    if rows == 0:
      return ServiceResult(GamesException.GameIDNotFound())
    return ServiceResult(updated_game)

  def remove_game(self, id: int) -> ServiceResult:
    rows = GamesCRUD(self.db).remove_game(id)
    if rows == None:
      return ServiceResult(GamesException.UnableToRemoveGame())
    if rows == 0:
      return ServiceResult(GamesException.GameIDNotFound())
    return ServiceResult({ 'id': id })

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
    except Exception as e:
      return None
