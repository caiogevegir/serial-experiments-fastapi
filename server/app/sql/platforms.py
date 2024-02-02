from database import execute_query, QueryType

# READ -------------------------------------------------------------------------

def list_platforms() -> list[tuple] | dict:
  query = '''
    SELECT *
    FROM platforms
  '''
  
  return execute_query(QueryType.READ, query)


# WRITE ------------------------------------------------------------------------

def add_platform(name: str, manufacturer: str, release_year: int) -> dict:
  query = f'''
    INSERT INTO platforms (name, manufacturer, release_year)
    VALUES ( '{name}', '{manufacturer}', {release_year} )
  '''
  
  return execute_query(QueryType.WRITE, query)
