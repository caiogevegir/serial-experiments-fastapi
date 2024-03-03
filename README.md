# serial-experiments-fastapi

Small backend project using `fastapi` and `sqlalchemy`.

## Pre-setup

- Install [SQLite](https://www.sqlite.org/) on your workstation and configure your server

## Setup

- Create a `.env` file on this project's root with your `SQLite` database configs:
```ini
SERVER_APP=main:app
SERVER_HOST=127.0.0.1
SERVER_PORT=8000
SERVER_LOGLEVEL=info

DATABASE_URL=sqlite+pysqlite:///./games_collection.db
```
- Install Python Requirements with `pip install -r requirements.txt`
- Run the application with `py server/app/main.py`
- Access `127.0.0.1:8000/docs` on your browser and have fun :)

## To Be Developed...

- Unit/Integration tests
