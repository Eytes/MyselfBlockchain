from app.pydantic_models import (
    block as block_model,
    chain as chain_model,
)


__chain = chain_model.Chain()


def get_chain() -> chain_model.Chain:
    return __chain


def sync():
    """
    Синхронизация локального блокчейна
    """


def insert_block(block: block_model.Block) -> int:
    """
    Вставка блока в конец списка
    :param block:
    :return позиция в списке блокчейна:
    """
    chain = get_chain()
    chain.blocks.append(block)
    return len(chain.blocks) - 1
