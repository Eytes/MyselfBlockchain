import hashlib
import os
from datetime import datetime

from app.pydantic_models import (
    block as block_model,
)

NUM_ZEROS = os.getenv('NUM_ZEROS')


def generate_header(block_details: block_model.BlockCreateHashField) -> str:
    """
    Создание заголовка для блока учитывая номер попытки
    :param block_details: необходимые данные для вычисления заголовка блока
    :param nonce: номер попытки вычислить нужный хеш
    """
    index = block_details.index
    prev_hash = block_details.previous_hash
    timestamp = block_details.timestamp
    data = block_details.data
    nonce = block_details.nonce
    return str(index) + prev_hash + data + str(timestamp) + str(nonce)


def calculate_hash(block_details: block_model.BlockCreateHashField) -> str:
    """
    Вычисление хеша блока учитывая номер попытки
    :param block_details: необходимые данные для вычисления заголовка блока
    :param nonce: номер попытки вычислить нужный хеш
    """
    header_string = generate_header(block_details)
    sha = hashlib.sha256()
    sha.update(header_string)
    return sha.hexdigest()


def mine(last_block: block_model.Block) -> block_model.Block:
    """
    Добыча блока
    :param last_block: последний блок в цепи
    """
    fields_for_block_hashing = block_model.BlockCreateHashField(
        index=last_block.index + 1,
        timestamp=datetime.now().timestamp(),
        data=f"I block {last_block.index + 1}",
        previous_hash=last_block.hash,
        nonce=0,
    )

    block_hash = calculate_hash(fields_for_block_hashing)
    while block_hash[0:NUM_ZEROS] != '0' * NUM_ZEROS:
        fields_for_block_hashing.nonce += 1
        block_hash = calculate_hash(fields_for_block_hashing)

    return block_model.Block(**fields_for_block_hashing.model_dump())
