import hashlib
import json
from typing import Optional

from app.core.redis_config import redis_client


def get_md5_async(content: bytes) -> str:
    """Generate an MD5 hash string for given content."""
    return hashlib.md5(content).hexdigest()


def get_cached_result(content: bytes) -> Optional[dict]:
    content_hash = get_md5_async(content)
    cached = redis_client.get(content_hash)
    if cached:
        cached_data = json.loads(cached.decode("utf-8"))
        cached_data["source"] = "cache"  # Cache'den alındığını belirt
        return cached_data
    return None
