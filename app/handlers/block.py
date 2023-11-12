import json

from app.pydantic_models import (
    block as block_model,
)


def convert_to_json_str(block: block_model.Block) -> str:
    return json.dumps(block.model_dump())


def get() -> block_model.Block: ...


def create_first() -> block_model.FirstBlock:
    first_block = block_model.FirstBlock(
        index=1,
        data="First block",
    )
    return first_block


def create() -> block_model.Block: ...
