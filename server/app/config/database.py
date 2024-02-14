import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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


def log_on_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()