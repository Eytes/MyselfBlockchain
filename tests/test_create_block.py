import pytest

from tests.fixtures import insert_empty_chain

from app.handlers import (
    block as block_handlers,
    chain as chain_handlers,
)


def test_create_first_block(insert_empty_chain):
    chain = insert_empty_chain
    assert len(chain.blocks) == 0

    first_block = block_handlers.create_first()
    chain.blocks.append(first_block)

    assert len(chain.blocks) == 1
