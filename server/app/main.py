import uvicorn
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from routers import games, platforms, developers
from errors.main import AppExceptionCase, app_exception_handler
from config.database import create_tables

# ------------------------------------------------------------------------------

load_dotenv()

ROUTERS = [ 
  games.router,
  platforms.router,
  developers.router
]

create_tables()

app = FastAPI()

@app.exception_handler(AppExceptionCase)
async def custom_app_exception_handler(request, e):
  return await app_exception_handler(request, e)

# Wildcard is only for study purposes, since the server is running locally
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"], 
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

for r in ROUTERS:
  app.include_router(r)

# ------------------------------------------------------------------------------

if __name__ == '__main__':
  uvicorn.run(
    app=os.getenv('SERVER_APP'), 
    host=os.getenv('SERVER_HOST'), 
    port=int(os.getenv('SERVER_PORT')), 
    log_level=os.getenv('SERVER_LOGLEVEL'), 
    reload=True
  )
