fastapi-tryout
==============

Just messing around with [FastAPI](https://fastapi.tiangolo.com/)
and [Pydantic](https://docs.pydantic.dev/).

## MySQL and table creation required
To use this, you'll need a MySQL-compatible database (I'm using MariaDB). Right
now the code expects it to be listening on a local socket at `/tmp/mysql.sock`.
You'll need to create the `accounts` table by running the
`fastapi_tryout/db/accounts.sql` script.

## Managed with Poetry
The project is using [Poetry](https://python-poetry.org) to manage dependencies
and its virtualenv. If you want the venv that Poetry creates to show up as an
option for Python interpreter in VS Code, you'll need to set an option to force
Poetry to create the venv inside the project directory, like so:

```
poetry config virtualenvs.in-project true
```

Then you can install the dependencies:
```
poetry install
```

And then run the server:
```
poetry run uvicorn fastapi_tryout.main:app
```

