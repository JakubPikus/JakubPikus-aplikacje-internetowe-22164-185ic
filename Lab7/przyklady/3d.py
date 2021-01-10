from redis import Redis

redis_connection = Redis(decode_responses=True)

redis_connection.set("klucz","wartoscdb0")

redis_connection_1 = Redis(decode_responses=True,db=1)

redis_connection_1.set("klucz","wartoscdb1")

print(redis_connection_1.get("klucz"))

print(redis_connection.get("klucz"))