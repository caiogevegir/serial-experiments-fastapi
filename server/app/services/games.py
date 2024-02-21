from main import AppService, AppCRUD, ServiceResult
from models.games import GamesModel
from schemas.games import GamesCreateSchema, GamesUpdateSchema
from errors.games import GamesException
from utils.enums import GameStatus, OwnershipStatus

# ------------------------------------------------------------------------------

class GamesService(AppService):

  def list_games(self, filters: dict) -> ServiceResult:
    games = GamesCRUD(self.db).list_games(filters)
    if games == None:
      return ServiceResult(GamesException.FailedToListGames())
    return ServiceResult(games)

  def list_games_by_developers(self, developer_id: int) -> ServiceResult:
    pass

  def add_game(self, game: GamesCreateSchema) -> ServiceResult:
    new_game = GamesCRUD(self.db).add_game(game)
    if new_game == None:
      return ServiceResult(GamesException.FailedToCreateGame())
    return ServiceResult(new_game)
  
  def update_game(self, game_id: int, params: dict) -> ServiceResult:
    rows = GamesCRUD(self.db).update_game(game_id, params)
    if rows == None:
      return ServiceResult(GamesException.FailedToUpdateGame())
    return ServiceResult(rows)

  def change_game_status(
    self, 
    game_id: int, 
    status: GameStatus
  ) -> ServiceResult:
    rows = GamesCRUD(self.db).change_game_status(game_id, status)
    if rows == None:
      return ServiceResult(GamesException.FailedToUpdateGame())
    return ServiceResult(rows)

  def change_game_platform(
    self,
    game_id: int,
    platform_id: int
  ) -> ServiceResult:
    rows = GamesCRUD(self.db).change_game_platform(game_id, platform_id)
    if rows == None:
      return ServiceResult(GamesException.FailedToUpdateGame())
    return ServiceResult(rows)

  def change_game_finish_date(
    self,
    game_id: int,
    finish_date: str
  ) -> ServiceResult:
    rows = GamesCRUD(self.db).change_game_finish_date(game_id, finish_date)
    if rows == None:
      return ServiceResult(GamesException.FailedToUpdateGame())
    return ServiceResult(rows)

  def change_game_ownership(
    self,
    game_id: int,
    ownership: OwnershipStatus
  ) -> ServiceResult:
    rows = GamesCRUD(self.db).change_game_ownership(game_id, ownership)
    if rows == None:
      return ServiceResult(GamesException.FailedToUpdateGame())
    return ServiceResult(rows)

  def remove_game(self, game_id: int) -> ServiceResult:
    rows = GamesCRUD(self.db).remove_game(game_id)
    if rows == None:
      return ServiceResult(GamesException.FailedToRemoveGame())
    return ServiceResult(rows)

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
  
  def update_game(self, game_id: int, params: dict) -> int | None:
    try:
      rows = self.db.query(GamesModel).filter_by(id=game_id).update(params)
      self.db.commit()
      return rows
    except:
      return None
  
  def remove_game(self, game_id: int) -> int | None:
    try:
      rows = self.db.query(GamesModel).delete(GamesModel.id == game_id)
      self.db.commit()
      return rows
    except:
      return None
