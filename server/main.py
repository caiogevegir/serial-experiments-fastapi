import uuid
import re
from enum import Enum
from datetime import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Wildcard is only for study purposes since the server is running locally
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"], 
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# ------------------------------------------------------------------------------

GAMES_CSV = './bucket/games.csv'
HISTORY_LOG = './bucket/history.log'

class Game(BaseModel):
  name: str
  platform: str
  status: str
  score: int | None

# GET --------------------------------------------------------------------------

@app.get('/games/detail')
def detail_game(id: str):
  output = None
  try:
    with open(GAMES_CSV, mode='r') as games_csv:
      while True:
        line = games_csv.readline()
        if not line:
          output = { 'error': 'Game not found' }
          break
        content = line.split(',')
        if content[0] == id:
          output = { 
            'id': content[0],
            'created_at': content[1],
            'updated_at': content[2], 
            'name': content[3], 
            'platform': content[4], 
            'status': content[5], 
            'score': content[6][:-1] # Removes \n at the end
          }
          break
  except Exception as e:
    output = { 'error': e }

  return output


@app.get('/games/list')
def list_games(platform: str = '', status: str = ''):
  output = []
  with open(GAMES_CSV, mode='r') as games_csv:
    while True:
      line = games_csv.readline()
      if not line:
        break
      content = line.split(',')

      match_filters = True
      if platform != '' and platform != content[4]:
        match_filters = False
      if status != '' and status != content[5]:
        match_filters = False

      if match_filters:
        output.append({
          'id': content[0],
          'created_at': content[1],
          'updated_at': content[2], 
          'name': content[3], 
          'platform': content[4], 
          'status': content[5], 
          'score': content[6][:-1] # Removes \n at the end
        })
  
  return output

# POST -------------------------------------------------------------------------

@app.post('/games/add')
def add_game(new_game: Game):
  output = None
  try:
    created_at = datetime.now()
    id = uuid.uuid4()
    with open(GAMES_CSV, mode='a') as games_csv:
      games_csv.write(
        f'{id},{created_at},{created_at},{new_game.name},{new_game.platform},{new_game.status},{new_game.score}\n'
      )
    output = { 'id': id, 'created_at': str(created_at) }
  except Exception as e:
    output = { 'error': e }

  return output

# PUT --------------------------------------------------------------------------

@app.put('/games/update')
def update_game(id: str, updated_game: Game):
  output = None
  try:
    with open(GAMES_CSV, mode='r') as games_csv:
      content = games_csv.read()
    updated_at = datetime.now()
    new_content = re.sub(
      rf'{id},([^,]*),.*', 
      rf'{id},\g<1>,{updated_at},{updated_game.name},{updated_game.platform},{updated_game.status},{updated_game.score}', 
      content
    )
    if content == new_content:
      output = { 'error': 'Game not found' }
    else:
      with open(GAMES_CSV, mode='w') as games_csv:
        games_csv.write(new_content)
      output = { 'id': id, 'updated_at': str(updated_at) }
  except Exception as e:
    output = { 'error': e }

  return output

# DELETE -----------------------------------------------------------------------

@app.delete('/games/remove')
def remove_game(id: str):
  output = None
  try:
    with open(GAMES_CSV, mode='r') as games_csv:
      content = games_csv.read()
    new_content = re.sub(rf'{id},.*\n', '', content)
    if content == new_content:
      output = { 'error': 'Game not found' }
    else:
      removed_at = datetime.now()
      with open(GAMES_CSV, mode='w') as games_csv:
        games_csv.write(new_content)
      output = { 'id': id, 'removed_at': str(removed_at) }
  except Exception as e:
    output = { 'error': e }

  return output
