from database import execute_query, QueryType

# READ -------------------------------------------------------------------------

def list_developers() -> dict:
  query = '''
  SELECT *
  FROM developers
  '''
  
  return execute_query(QueryType.READ, query)

# WRITE ------------------------------------------------------------------------

def add_developer(name: str, country_code: str) -> dict:
  query = f'''
  INSERT INTO developers ( name, country_code )
  VALUES ( '{name}', '{country_code}' )
  '''

  return execute_query(QueryType.WRITE, query)
