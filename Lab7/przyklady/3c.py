from redis import Redis

redis_connection = Redis(decode_responses=True)

list_key ="lista"

while True:
    print(redis_connection.brpop(list_key))