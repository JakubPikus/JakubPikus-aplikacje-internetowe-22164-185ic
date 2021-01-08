from redis import Redis

redis_connection = Redis(decode_responses=True)

redis_connection.set("klucz","wartosc")

redis_connection_1 = Redis(decode_responses=True)

print(redis_connection_1.get("klucz"))

print(redis_connection.get("klucz"))