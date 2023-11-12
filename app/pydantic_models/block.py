import datetime
import uuid
from typing import Any

from pydantic import (
    BaseModel,
    Field,
)

from app.utils import (
    get_hash,
)


class FirstBlock(BaseModel):
    index: int
    timestamp: float = Field(default=datetime.datetime.now().timestamp())
    previous_hash: None = None
    data: Any  # TODO: указать настоящий тип данных


class Block(BaseModel):
    index: int
    timestamp: float
    previous_hash: str
    hash: str
    data: Any  # TODO: указать настоящий тип данных
    nonce: int


class CreatedBlockIndex(BaseModel):
    index: int


class BlockCreateHashField(BaseModel):
    index: int
    timestamp: float
    previous_hash: str
    data: Any  # TODO: указать настоящий тип данных
    nonce: int
