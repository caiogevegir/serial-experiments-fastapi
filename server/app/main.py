import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

import database
from routers import games, platforms, developers

# ------------------------------------------------------------------------------

MAIN_APP = 'main:app'
HOST = '127.0.0.1'
PORT = 8000
LOG_LEVEL = 'info'
RELOAD = True

ROUTERS = [ 
  games.router,
  platforms.router,
  developers.router
]

@asynccontextmanager
async def lifespan(app: FastAPI):
  # Setup
  database.init()
  yield
  # Teardown

app = FastAPI(lifespan=lifespan)

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
    app=MAIN_APP, 
    host=HOST, 
    port=PORT, 
    log_level=LOG_LEVEL, 
    reload=RELOAD
  )
