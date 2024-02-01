import os
from enum import Enum
from mysql.connector import MySQLConnection, Error
from dotenv import load_dotenv

load_dotenv()

class QueryType(Enum):
  READ = 0
  WRITE = 1

AUTH_PLUGIN = 'mysql_native_password'
SUCCESS_CONNECTION_MSG = 'MySQL Database connection successful'
SUCCESS_QUERY_MSG = 'Query successful'
DB_ERROR_KEY = 'db_error'

HOST = os.getenv('MYSQL_HOST')
USER = os.getenv('MYSQL_USER')
PASS = os.getenv('MYSQL_PASSWORD')
DB_NAME = os.getenv('MYSQL_DB')

CREATE_DATABASE_QUERY = f'''
  CREATE DATABASE IF NOT EXISTS {DB_NAME};
'''

USE_DATABASE_QUERY = f'''
  USE {DB_NAME};
'''

CREATE_DEVELOPERS_TABLE_QUERY = '''
  CREATE TABLE IF NOT EXISTS developers (
    id SMALLINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    country_code VARCHAR(2) NOT NULL
  );
'''

CREATE_PLATFORMS_TABLE_QUERY = '''
  CREATE TABLE IF NOT EXISTS platforms (
    id SMALLINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    manufacturer VARCHAR(50) NOT NULL,
    release_year SMALLINT CHECK ( release_year BETWEEN 1900 AND 2999 )
  );
'''

CREATE_GAMES_TABLE = '''
  CREATE TABLE IF NOT EXISTS games (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(60) NOT NULL,
    platform_id SMALLINT, FOREIGN KEY (platform_id) REFERENCES platforms(id) ON DELETE SET NULL,
    gameplay_status ENUM('BACKLOG', 'PLAYING', 'HIATUS', 'FINISHED', 'DROPPED') NOT NULL,
    is_owned BOOL NOT NULL,
    commentary VARCHAR(255),
    backlog_date DATE NOT NULL,
    start_date DATE,
    finish_date DATE,
    score TINYINT CHECK ( score BETWEEN 0 AND 10 )
  );
'''

CREATE_GAMES_BY_DEVELOPER_TABLE_QUERY = '''
  CREATE TABLE IF NOT EXISTS games_by_developers (
    game_id VARCHAR(36), FOREIGN KEY (game_id) REFERENCES games(id) ON DELETE CASCADE,
    developer_id SMALLINT, FOREIGN KEY (developer_id) REFERENCES developers(id) ON DELETE CASCADE
  );
'''

INIT_DB_QUERIES = [
  CREATE_DATABASE_QUERY,
  USE_DATABASE_QUERY,
  CREATE_DEVELOPERS_TABLE_QUERY,
  CREATE_PLATFORMS_TABLE_QUERY,
  CREATE_GAMES_TABLE,
  CREATE_GAMES_BY_DEVELOPER_TABLE_QUERY
]

# ------------------------------------------------------------------------------

def init() -> None:
  try:
    conn = MySQLConnection(
      host=HOST,
      user=USER,
      passwd=PASS,
      auth_plugin=AUTH_PLUGIN
    )
    cursor = conn.cursor()
    for q in INIT_DB_QUERIES:
      cursor.execute(q)
      conn.commit()
    cursor.close()
    conn.close()
    print(SUCCESS_CONNECTION_MSG)
  except Error as err:
    print('MySQL Error: ', err)

# ------------------------------------------------------------------------------

def connect_to_database() -> MySQLConnection:
  return MySQLConnection(
    host=HOST,
    user=USER,
    passwd=PASS,
    database=DB_NAME,
    auth_plugin=AUTH_PLUGIN
  )


def execute_query(type: QueryType, query: str) -> list | dict:
  ret = {}
  try:
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute(query)

    match type:
      case QueryType.READ: # Receives the items
        ret = cursor.fetchall()
      case QueryType.WRITE: # Commits the changes
        conn.commit()

    cursor.close()
    conn.close()
  except Error as err:
    ret[DB_ERROR_KEY] = err
  
  return ret
