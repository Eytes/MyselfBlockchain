import datetime
import uuid
from typing import Any

from pydantic import (
    BaseModel,
    Field,
)


class FirstBlock(BaseModel):
    id: uuid.UUID = Field(default=uuid.uuid4())
    timestamp: float = Field(default=datetime.datetime.now().timestamp())
    previous_hash: None = None
    data: Any  # TODO: указать настоящий тип данных


class Block(BaseModel):
    id: uuid.UUID = Field(default=uuid.uuid4())
    timestamp: float = Field(default=datetime.datetime.now().timestamp())
    previous_hash: str
    hash: str
    data: Any  # TODO: указать настоящий тип данных


class CreatedBlockUUID(BaseModel):
    id: uuid.UUID


class BlockCreateFields(BaseModel):
    previous_hash: str
    hash: str
    data: Any  # TODO: указать настоящий тип данных
