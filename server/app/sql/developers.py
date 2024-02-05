from database import execute_query, QueryType

# READ -------------------------------------------------------------------------

def list_developers() -> tuple:
  query = '''
    SELECT *
    FROM developers
  '''
  
  return execute_query(QueryType.READ, query)

# WRITE ------------------------------------------------------------------------

def add_developer(name: str, country_code: str) -> tuple:
  query = f'''
    INSERT INTO developers ( name, country_code )
    VALUES ( %s, %s )
  '''

  return execute_query(QueryType.WRITE, query, (name, country_code))
