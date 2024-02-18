from main import AppExceptionCase

# ------------------------------------------------------------------------------

class GamesException:

  class FailedToListGames(AppExceptionCase):
    def __init__(self, context: dict = None):
      status_code = 500
      AppExceptionCase.__init__(self, status_code, context)
  
  class FailedToGetGame(AppExceptionCase):
    def __init__(self, context: dict = None):
      status_code = 500
      AppExceptionCase.__init__(self, status_code, context)
  
  class MultipleGamesWithSameID(AppExceptionCase):
    def __init__(self, context: dict = None):
      status_code = 500
      AppExceptionCase.__init__(self, status_code, context)
  
  class FailedToCreateGame(AppExceptionCase):
    def __init__(self, context: dict = None):
      status_code = 500
      AppExceptionCase.__init__(self, status_code, context)
  
  class FailedToUpdateGame(AppExceptionCase):
    def __init__(self, context: dict = None):
      status_code = 500
      AppExceptionCase.__init__(self, status_code, context)

  class FailedToRemoveGame(AppExceptionCase):
    def __init__(self, context: dict = None):
      status_code = 500
      AppExceptionCase.__init__(self, status_code, context)
