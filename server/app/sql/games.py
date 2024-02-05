from database import execute_query, QueryType

# READ -------------------------------------------------------------------------

def list_games(
  platform_id: int | None, 
  developer_id: int | None, 
  gameplay_status: str | None
) -> dict:
  
  params = tuple()

  query = '''
    SELECT 
      games.id, 
      games.name, 
      platforms.name, 
      games.gameplay_status,
      games.score
    FROM games INNER JOIN platforms ON games.platform_id = platforms.id\n
  '''

  if platform_id != None:
    search_keyword = 'WHERE' if params == () else 'AND'
    params += (platform_id,)
    query += f'{search_keyword} platform_id = %s\n'
  
  if gameplay_status != None:
    search_keyword = 'WHERE' if params == () else 'AND'
    params += (gameplay_status,)
    query += f'{search_keyword} gameplay_status = %s\n'
  
  if developer_id != None:
    search_keyword = 'WHERE' if params == () else 'AND'
    params += (developer_id,)
    query += f'''{search_keyword} id IN (
        SELECT game_id
        FROM games_by_developers
        WHERE developer_id = %s
      )\n
    '''

  return execute_query(QueryType.READ, query, params)


def detail_game(game_id: str) -> tuple:
  query = f'''
    SELECT 
      games.id, 
      games.name, 
      platforms.name AS platform,
      games.gameplay_status,
      GROUP_CONCAT(developers.name) AS developers,
      games.is_owned, 
      games.commentary, 
      games.backlog_date, 
      games.start_date, 
      games.finish_date, 
      games.score
    FROM games 
    INNER JOIN platforms ON games.platform_id = platforms.id
    INNER JOIN games_by_developers ON games.id = games_by_developers.game_id
    INNER JOIN developers ON games_by_developers.developer_id = developers.id
    WHERE games.id = %s
  '''

  return execute_query(QueryType.READ, query, (game_id,))
  
# WRITE ------------------------------------------------------------------------

def add_game(    
  game_id: str,
  name: str,
  platform_id: int,
  gameplay_status: str,
  is_owned: bool,
  backlog_date: str,
  commentary: bool | None = None,
  start_date: str | None = None,
  finish_date: str | None = None,
  score: int | None = None
) -> tuple:
  query = f'''
    INSERT INTO games
    VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )
  '''
  params = ( 
    game_id, name, platform_id, gameplay_status, is_owned, commentary, 
    backlog_date, start_date, finish_date, score
  )

  return execute_query(QueryType.WRITE, query, params)


def assign_game_to_developers(game_id: str, developers: list[str]) -> tuple:
  query = f'''
    INSERT INTO games_by_developers
    VALUES
  '''
  params = tuple()

  for developer_id in developers:
    query += f'( %s, %s ),'
    params += ( game_id, developer_id )
  query = query[:-1] # Removes last ','
  
  return execute_query(QueryType.WRITE, query, params)


def update_game() -> dict:
  pass


def delete_game() -> dict:
  pass
