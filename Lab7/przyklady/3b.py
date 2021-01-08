from redis import Redis


redis_connection = Redis(decode_responses=True)

list_key ="lista"

redis_connection.rpush(list_key,1,4,7,10,13)

print(redis_connection.lrange(list_key,2,4))