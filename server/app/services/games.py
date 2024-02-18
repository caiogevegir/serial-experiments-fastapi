from main import AppService, AppCRUD, ServiceResult
from models.games import GamesModel
from schemas.games import GamesCreateSchema, GamesUpdateSchema
from errors.games import GamesException
from utils.enums import GameStatus, OwnershipStatus

# ------------------------------------------------------------------------------

class GamesService(AppService):

  def list_all_games(self) -> ServiceResult:
    games = GamesCRUD(self.db).list_all_games()
    if games == None:
      return ServiceResult(GamesException.FailedToListGames())
    return ServiceResult(games)

  def list_games_by_status(self, status: GameStatus) -> ServiceResult:
    games = GamesCRUD(self.db).list_games_by_status(status)
    if games == None:
      return ServiceResult(GamesException.FailedToListGames())
    return ServiceResult(games)

  def list_games_by_ownership(
    self, 
    ownership: OwnershipStatus
  ) -> ServiceResult:
    games = GamesCRUD(self.db).list_games_by_ownership(ownership)
    if games == None:
      return ServiceResult(GamesException.FailedToListGames())
    return ServiceResult(games)

  def list_games_by_platform(self, platform_id: int) -> ServiceResult:
    games = GamesCRUD(self.db).list_games_by_platform(platform_id)
    if games == None:
      return ServiceResult(GamesException.FailedToListGames())
    return ServiceResult(games)

  def list_games_by_developers(self, developer_id: int) -> ServiceResult:
    pass

  def get_game_by_id(self, game_id: int) -> ServiceResult:
    games = GamesCRUD(self.db).get_game_by_id(game_id)
    if games == None:
      return ServiceResult(GamesException.FailedToGetGame())
    if len(games) > 1:
      return ServiceResult(GamesException.MultipleGamesWithSameID())
    return ServiceResult(games)

  def add_game(self, game: GamesCreateSchema) -> ServiceResult:
    new_game = GamesCRUD(self.db).add_game(game)
    if new_game == None:
      return ServiceResult(GamesException.FailedToCreateGame())
    return ServiceResult(new_game)

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

  def list_all_games(self) -> list[GamesModel] | None:
    try:
      return self.db.query(GamesModel).all()
    except:
      return None
  
  def list_games_by_status(self, status: GameStatus) -> list[GamesModel] | None:
    try:
      return self.db.query(GamesModel).filter_by(status=status.value).all()
    except:
      return None
  
  def list_games_by_ownership(
    self, 
    ownership: OwnershipStatus
  ) -> list[GamesModel] | None:
    try:
      return self.db.query(GamesModel) \
        .filter_by(ownership=ownership.value).all()
    except:
      return None
  
  def list_games_by_platform(self, platform_id: int) -> list[GamesModel] | None:
    try:
      return self.db.query(GamesModel).filter_by(platform_id=platform_id).all()
    except:
      return None
    
  def get_game_by_id(self, game_id: int) -> list[GamesModel] | None:
    try:
      return self.db.query(GamesModel).filter_by(id=game_id).all()
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
  
  def change_game_status(
    self, 
    game_id: int, 
    status: GameStatus
  ) -> int | None:
    try:
      rows = self.db.query(GamesModel) \
        .filter_by(id=game_id).update({ 'status': status.value })
      self.db.commit()
      return rows
    except:
      return None
  
  def change_game_platform(
    self,
    game_id: int,
    platform_id: int
  ) -> int | None:
    try:
      rows = self.db.query(GamesModel) \
        .filter_by(id=game_id).update({ 'platform_id': platform_id })
      self.db.commit()
      return rows
    except:
      return None
  
  def change_game_finish_date(
    self,
    game_id: int,
    finish_date: str
  ) -> int | None:
    try:
      rows = self.db.query(GamesModel) \
        .filter_by(id=game_id).update({ 'finish_date': finish_date })
      self.db.commit()
      return rows
    except:
      return None
  
  def change_game_ownership(
    self,
    game_id: int,
    ownership: OwnershipStatus
  ) -> int | None:
    try:
      rows = self.db.query(GamesModel) \
        .filter_by(id=game_id).update({ 'ownership': ownership.value })
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
