from fastapi import APIRouter

from app.pydantic_models import (
    block as block_model,
)


router = APIRouter(
    prefix='/api/block',
    tags=["Block"],
)


@router.post(
    path='/create',
)
def create_block(): ...
