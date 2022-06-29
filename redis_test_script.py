import redis
print("hello redis-py")
r = redis.Redis(host="mtglandcalculator_db_1", port=6379, db=0)
r.set('z', 'Successss!!')
a = r.get('z')
print(f"I got a {a} from redis")
