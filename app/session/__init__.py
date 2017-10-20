import os, json, redis

REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ['REDIS_PORT']

r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)

def getSession(token):
    result = r.get(token)
    if result is not None:
        return json.loads(result)
    return {}
