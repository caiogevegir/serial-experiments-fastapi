from database import execute_query, QueryType

#==============================================================================#
# READ                                                                         #
#==============================================================================#

def list_platforms() -> tuple:
  query = '''
    SELECT *
    FROM platforms
  '''
  
  return execute_query(QueryType.READ, query)

#==============================================================================#
# WRITE                                                                        #
#==============================================================================#

def add_platform(name: str, manufacturer: str, release_year: int) -> tuple:
  query = f'''
    INSERT INTO platforms (name, manufacturer, release_year)
    VALUES ( %s, %s, %s )
  '''
  
  return execute_query(
    QueryType.WRITE, 
    query, 
    (name, manufacturer, release_year)
  )
