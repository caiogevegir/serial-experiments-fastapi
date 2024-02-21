from sqlalchemy.orm import Session
from errors.main import AppExceptionCase

# ------------------------------------------------------------------------------

class DBSessionMixin:
  def __init__(self, db: Session):
    self.db = db


class AppService(DBSessionMixin):
  pass


class AppCRUD(DBSessionMixin):
  pass

# ------------------------------------------------------------------------------

class ServiceResult:
  def __init__(self, arg):
    if isinstance(arg, AppExceptionCase):
      self.success = False
      self.exception_case = arg.exception_case
      self.status_code = arg.status_code
    else:
      self.success = True
      self.exception_case = None
      self.status_code = None
    self.value = arg

  def __str__(self):
    if self.success:
      return "[Success]"
    return f'[Exception] "{self.exception_case}"'

  def __repr__(self):
    if self.success:
      return "<ServiceResult Success>"
    return f"<ServiceResult AppException {self.exception_case}>"

  def __enter__(self):
    return self.value

  def __exit__(self, *kwargs):
    pass

  def handle_result(self):
    if not self.success:
      with self as exception:
        raise exception
    with self as result:
      return result
