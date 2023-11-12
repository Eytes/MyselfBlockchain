import hashlib


def get_hash(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()
