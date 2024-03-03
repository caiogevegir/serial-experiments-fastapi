from .main import AppService, ServiceResult

from repositories.games import GamesCRUD
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
