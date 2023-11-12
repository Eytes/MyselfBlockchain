import json
import uuid

from app.pydantic_models import (
    block as block_model,
)
from app.handlers import (
    chain as chain_handlers,
)


def convert_to_json_str(block: block_model.Block) -> str:
    return json.dumps(block.model_dump())


def get() -> block_model.Block: ...


def create_first() -> block_model.FirstBlock:
    first_block = block_model.FirstBlock(data="First block")
    return first_block


def create(block: block_model.BlockCreateFields) -> block_model.CreatedBlockUUID: ...


