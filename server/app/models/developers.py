from sqlalchemy import Column, Integer, String

from config.database import Base

# ------------------------------------------------------------------------------

class DevelopersModel(Base):
  __tablename__ = 'developers'

  id = Column(
    'id', 
    Integer, 
    primary_key=True,
    autoincrement='auto'
  )

  name = Column(
    'name',
    String(30),
    unique=True,
    nullable=False
  )

  country_code = Column(
    'country_code',
    String(2),
    nullable=False
  )
