# serial-experiments-fastapi

Small backend project using `fastapi` and `MySQL`.

## Pre-setup

- Install [MySQL](https://www.mysql.com/) on your workstation and configure your server

## Setup

- Create a `.env` file on this project's root with your `MySQL` credentials
```ini
MYSQL_HOST=
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_DB=games_collection
```
- Install Python Requirements with `pip install requirements.txt`
- Run the application with `py server/app/main.py`
- Access `127.0.0.1:8000/docs` on your browser and have fun :)

## To Be Developed...

- Unit/Integration tests
- Authentication methods
