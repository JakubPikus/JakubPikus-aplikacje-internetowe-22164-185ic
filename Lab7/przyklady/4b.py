from redis import Redis

redis_connection = Redis(decode_responses=True)

redis_connection.zadd("posortowane_klucze",{"klucz1": 1})
redis_connection.zadd("posortowane_klucze",{"klucz2": 6})
redis_connection.zadd("posortowane_klucze",{"klucz3": 2})
redis_connection.zadd("posortowane_klucze",{"klucz4": 4})

print(redis_connection.zrange("posortowane_klucze",0, -1, withscores = True))