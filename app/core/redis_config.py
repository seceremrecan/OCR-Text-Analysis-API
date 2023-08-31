import redis

# Redis config
REDIS_HOST = "redis"
REDIS_PORT = 6379

# Redis'e bağlantı oluştur
redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
