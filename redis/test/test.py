import redis

redis_connection = redis.StrictRedis(host = '192.168.99.100', port = 6379, db = 0)

#append Hello World in 'message' key
for x in 'Hello World':
    redis_connection.append('message', x)

print("'message' value: ", redis_connection.get('message'))
print('db size: ', redis_connection.dbsize())

print("delete 'message' key")
redis_connection.delete('message')
print('db size: ', redis_connection.dbsize())

#print all keys
print(redis_connection.keys('*'))