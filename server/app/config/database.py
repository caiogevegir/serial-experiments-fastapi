import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv

# ------------------------------------------------------------------------------

load_dotenv()

engine = create_engine(
  url=os.getenv('DATABASE_URL'),
  connect_args={ 'check_same_thread': False }, # For SQLite
  echo=True
)

SessionLocal = sessionmaker(
  autocommit=False,
  autoflush=False,
  bind=engine
)

Base = declarative_base()

# ------------------------------------------------------------------------------

class DBSessionMixin:
  def __init__(self, db: Session):
    self.db = db

# ------------------------------------------------------------------------------

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

def create_tables():
  Base.metadata.create_all(bind=engine)
