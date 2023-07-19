#!/usr/bin/env python3

import redis
import uuid
from typing import Union

class Cache:
    def __init__(self):
        # Create a private variable _redis and initialize it with a Redis client
        self._redis = redis.Redis()
        # Flush the Redis instance using flushdb
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        # Generate a random key using uuid
        key = str(uuid.uuid4())
        # Store the input data in Redis using the random key
        self._redis.set(key, data)
        # Return the key as a string
        return key

# Test the Cache class
if __name__ == "__main__":
    cache = Cache()

    data = b"hello"
    key = cache.store(data)
    print(key)

    local_redis = redis.Redis()
    print(local_redis.get(key))
