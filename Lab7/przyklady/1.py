from redis import Redis
redis_connection = Redis()
print("Połączony do serwera Redis: ", redis_connection.ping())