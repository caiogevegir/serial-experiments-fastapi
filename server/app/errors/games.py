from main import AppExceptionCase

# ------------------------------------------------------------------------------

class GamesException:

  class UnableToListGames(AppExceptionCase):
    def __init__(self, context: dict = None):
      status_code = 500
      AppExceptionCase.__init__(self, status_code, context)
  
  class UnableToCreateGame(AppExceptionCase):
    def __init__(self, context: dict = None):
      status_code = 500
      AppExceptionCase.__init__(self, status_code, context)
  
  class UnableToUpdateGame(AppExceptionCase):
    def __init__(self, context: dict = None):
      status_code = 500
      AppExceptionCase.__init__(self, status_code, context)
  
  class GameIDNotFound(AppExceptionCase):
    def __init__(self, context: dict = None):
      status_code = 400
      AppExceptionCase.__init__(self, status_code, context)

  class UnableToRemoveGame(AppExceptionCase):
    def __init__(self, context: dict = None):
      status_code = 500
      AppExceptionCase.__init__(self, status_code, context)
