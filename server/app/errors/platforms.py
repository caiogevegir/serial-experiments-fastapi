from main import AppExceptionCase

class PlatformsException:

  class FailedToListPlatforms(AppExceptionCase):
    def __init__(self, context: dict = None):
      status_code = 500
      AppExceptionCase.__init__(self, status_code, context)
 
  class FailedToAddPlatform(AppExceptionCase):
    def __init__(self, context: dict = None):
      status_code = 500
      AppExceptionCase.__init__(self, status_code, context)
