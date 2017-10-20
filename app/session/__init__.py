import os, json, redis

HOST = os.environ['REDIS_HOST']
PORT = os.environ['REDIS_PORT']
PASSWORD = os.environ['REDIS_PASSWORD']

r = redis.StrictRedis(host=HOST, port=PORT, db=0, password=PASSWORD)

def getSession(token):
    result = r.get(token)
    if result is not None:
        return json.loads(result)
    return {}
