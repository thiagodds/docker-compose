import redis

redis_connetion = redis.StrictRedis(host = '192.168.99.100', port = 6379, db = 0)

redis_connetion.set('foo', 'bar')

print(redis_connetion.get('foo'))