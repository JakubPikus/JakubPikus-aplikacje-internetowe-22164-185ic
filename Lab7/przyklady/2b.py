from redis import Redis


redis_connection = Redis(decode_responses=True) 
key ="kluczv2"
value ="wartoscv2"
redis_connection.set(key, value)
print(redis_connection.get(key))