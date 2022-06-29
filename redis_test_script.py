import redis
print("hello redis-py")
#r = redis.Redis(host="db", port=6379, db=0)
r = redis.Redis(host="localhost", port=6379, db=0)

card = {"Name":"Elvish Mystic", "cost":"0", "isLand":"F", "edhrank":123, "legality":["whatever", "modenr", "legacy"]}

#r.set('z', 'Successss!!')
r.hmset("Elvish Mystic", card)
#a = r.get('a')
a = r.hgetall("Elvish Mystic")
print(f"I got a {a[b'edhrank'].decode('utf-8')} from redis")
