from redis import Redis

redis_connection = Redis()

key ="klucz"
value ="wartosc"

redis_connection.set(key, value)
print(redis_connection.get(key))