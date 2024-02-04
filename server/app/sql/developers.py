from database import execute_query, QueryType

# READ -------------------------------------------------------------------------

def list_developers() -> tuple(dict | list | None, str | None):
  query = '''
    SELECT *
    FROM developers
  '''
  
  return execute_query(QueryType.READ, query)

# WRITE ------------------------------------------------------------------------

def add_developer(
  name: str, 
  country_code: str
) -> tuple(dict | None, str | None):
  query = f'''
    INSERT INTO developers ( name, country_code )
    VALUES ( ?, ? )
  '''

  return execute_query(QueryType.WRITE, query, (name, country_code))
