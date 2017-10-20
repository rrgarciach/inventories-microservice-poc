import redis

r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

def getSession(token):
    result = r.get(token)
    if result is not None:
        return json.loads(result)
    return {}
