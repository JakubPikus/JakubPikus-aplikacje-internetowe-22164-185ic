from redis import Redis

redis_connection = Redis(decode_responses=True)

redis_connection.sadd("klucz","wartosc1")
redis_connection.sadd("klucz","wartosc2")
redis_connection.sadd("klucz","wartosc3")

print(redis_connection.smembers("klucz"))