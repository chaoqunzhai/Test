import redis

r = redis.Redis(host='localhost', port=6379)
r.set('foor','Bar')

print(r.get('foor'))