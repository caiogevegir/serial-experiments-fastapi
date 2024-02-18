from main import AppExceptionCase

# ------------------------------------------------------------------------------

class DevelopersException:
  
  class FailedToListDevelopers(AppExceptionCase):
    def __init__(self, context: dict = None):
      status_code = 500
      AppExceptionCase.__init__(self, status_code, context)
  
  class FailedToAddDevelopers(AppExceptionCase):
    def __init__(self, context: dict = None):
      status_code = 500
      AppExceptionCase.__init__(self, status_code, context)