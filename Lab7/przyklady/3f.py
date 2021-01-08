from redis import Redis
from time import sleep
from datetime import datetime

redis_connection = Redis(decode_responses=True)

redis_connection.set("klucz","wartosc")
redis_connection.expire("klucz",30)

print(datetime.now().time(), redis_connection.get("klucz"))
sleep(5)
print(datetime.now().time(), redis_connection.get("klucz"))
sleep(10)
print(datetime.now().time(), redis_connection.get("klucz"))