from database import execute_query, QueryType

# READ -------------------------------------------------------------------------

def list_platforms() -> tuple(dict | list | None, str | None):
  query = '''
    SELECT *
    FROM platforms
  '''
  
  return execute_query(QueryType.READ, query)


# WRITE ------------------------------------------------------------------------

def add_platform(
  name: str, 
  manufacturer: str, 
  release_year: int
) -> tuple(dict | list | None, str | None):
  query = f'''
    INSERT INTO platforms (name, manufacturer, release_year)
    VALUES ( ?, ?, ? )
  '''
  
  return execute_query(
    QueryType.WRITE, 
    query, 
    (name, manufacturer, release_year)
  )
