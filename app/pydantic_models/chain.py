from pydantic import (
    BaseModel,
    Field,
)

from app.pydantic_models import (
    block as block_model,
)


class Chain(BaseModel):
    blocks: list[block_model.Block] = Field(default=[])



