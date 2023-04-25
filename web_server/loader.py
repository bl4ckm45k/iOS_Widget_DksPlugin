import redis.asyncio as redis

from config import load_config

config = load_config()
redis_cli = redis.Redis(decode_responses=True)
