import pytest

from app.pydantic_models.chain import Chain


@pytest.fixture
def insert_empty_chain() -> Chain:
    return Chain()
