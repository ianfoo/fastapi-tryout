import uuid
from datetime import datetime
from enum import Enum
from typing import Annotated, Optional

from fastapi import FastAPI
from mysql.connector import connect
from pydantic import BaseModel, Field, UUID4

app = FastAPI()


class Blockchain(str, Enum):
    ETH = "eth"
    TETH = "eth-goerli"
    BTC = "btc-mainnet"
    TBTC = "btc-testnet"


class CreateAccountRequest(BaseModel):
    uuid: UUID4 = Field(default_factory=uuid.uuid4)
    label: str = Field(
        ...,
        title="Account name",
        description="Name of the account",
        min_length=3,
        max_length=200,
    )
    chain: Blockchain
    vault_uuid: UUID4


class Account(CreateAccountRequest):
    """Includes fields not known at creation time."""

    id: int
    created_at: datetime
    updated_at: datetime


@app.get("/hello")
def say_hello():
    return {"message": "Hello World!"}


@app.get("/hello/{name}")
def say_hello_to(name: Annotated[str | None, "Name of the person"]):
    if name is None:
        name = "you"
    return {"message": f"Hello {name}!"}


@app.post("/account")
def api_create_account(request: CreateAccountRequest):
    account_id = create_account(request)
    return {"id": account_id}


@app.get("/account/{id}")
def account(id: int):
    account = get_account(id)
    return account


class Database:
    def __enter__(
        self,
        conn_args: dict[str, str | int] = {
            "database": "test",
            "unix_socket": "/tmp/mysql.sock",
        },
    ):
        self.conn = connect(**conn_args)
        self.cursor = self.conn.cursor(dictionary=True)
        return self.conn, self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()

        if exc_val:
            raise exc_val


def create_account(request: CreateAccountRequest) -> int:
    query = (
        "INSERT INTO accounts (uuid, label, chain, vault_uuid) VALUES (%s, %s, %s, %s)"
    )
    values = (
        str(request.uuid),
        request.label,
        request.chain.value,
        str(request.vault_uuid),
    )
    with Database() as (cnx, cursor):
        cursor.execute(query, values)
        cnx.commit()

        account_id = cursor.lastrowid
        return account_id


def get_account(id: int) -> Optional[Account]:
    query = "SELECT * FROM accounts WHERE id = %s"
    values = (id,)
    with Database() as (_, cursor):
        cursor.execute(query, values)
        account = cursor.fetchone()
        if account:
            return Account(**account)
