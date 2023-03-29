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
```sh
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
```sh
poetry config virtualenvs.in-project true
```

Then you can install the dependencies:
```sh
poetry install
```

And then run the server:
```sh
poetry run uvicorn fastapi_tryout.main:app
```

## Interacting with the server

The server exposes a couple example endpoints, including a basic `/hello` hello
world endpoint, and a `/hello/{name}` endpoint that will greet a user with a
provided name:
```sh
❯ http :8000/hello/ian
HTTP/1.1 200 OK
content-length: 24
content-type: application/json
date: Wed, 29 Mar 2023 23:04:35 GMT
server: uvicorn

{
    "message": "Hello ian!"
}
```

There are also two endpoints to perform the CR operations (from the larger CRUD
set) for a rudimentary "account."
```sh
❯ http post :8000/account label="My Account" chain="eth" vault_uuid=25b1d018-cce7-42ba-b411-483abddd212d
HTTP/1.1 200 OK
content-length: 8
content-type: application/json
date: Wed, 29 Mar 2023 23:10:43 GMT
server: uvicorn

{
    "id": 1
}


❯ http :8000/account/1
HTTP/1.1 200 OK
content-length: 211
content-type: application/json
date: Wed, 29 Mar 2023 23:11:09 GMT
server: uvicorn

{
    "chain": "eth",
    "created_at": "2023-03-29T16:10:43",
    "id": 1,
    "label": "My Account",
    "updated_at": "2023-03-29T16:10:43",
    "uuid": "0d8f30cf-3568-4a7b-bfab-ad2ba5082593",
    "vault_uuid": "25b1d018-cce7-42ba-b411-483abddd212d"
}
```

(If you're wondering what the client here is, it's
[HTTPie](https://httpie.io/cli).)
