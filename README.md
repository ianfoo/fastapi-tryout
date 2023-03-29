fastapi-tryout
==============

Just messing around with [FastAPI](https://fastapi.tiangolo.com/)
and [Pydantic](https://docs.pydantic.dev/).

## MySQL and table creation required
To use this, you'll need a MySQL-compatible database (I'm using MariaDB). Right
now the code expects it to be listening on a local socket at `/tmp/mysql.sock`.
Just edit the code if you need to connect somewhere else or as a different user:
see the [MySQL Connector
documentation](https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html)
for more info on the connect parameters.

Before you can run the server, You'll need to create the `fastapi_tryout`
database and `accounts` table by running the `database.sql` script as a
privileged user (the default user from a Homebrew MariaDB installation worked
fine here), like so:
```
< database.sql mariadb
```
Note that there is _nothing secure_ about this database configuration!  Do not
run this anywhere that matters! This is just a simple setup for the purposes of
this tryout.

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
