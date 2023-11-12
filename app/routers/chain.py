from fastapi import APIRouter

from app.pydantic_models import (
    block as block_model,
)


router = APIRouter(
    prefix='/api/chain',
    tags=["Chain"],
)


@router.post(
    path='/add_block',
)
def add_block(block: block_model.Block): ...
