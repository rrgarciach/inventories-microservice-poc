from flask import Flask, request, jsonify
import redis
import logging, os, json

REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ['REDIS_PORT']
r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)

def request_wants_json():
    best = request.accept_mimetypes \
        .best_match(['application/json', 'text/html'])
    return best == 'application/json' and \
        request.accept_mimetypes[best] > \
        request.accept_mimetypes['text/html']

def create_app():
    app = Flask(__name__)

    @app.route('/api/v1/orders', methods=['GET'])
    def getAllOrders():
        if request_wants_json():
            # return jsonify({"message": 'hello!'})
            session = loadSession()
            return jsonify(session)
        return 'no json'

    return app

def loadSession():
    response = r.get('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiJmb28xMjMiLCJyb2xlIjoiY2xpZW50IiwiaWF0IjoxNTA4NTI0MzYwLCJleHAiOjE1MDg1MjUyNjB9.UcGkf2nEQvBwtXy_BKTXrCehGz0BuqXmlXtf8hiiR1o')
    r.set('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiJmb28xMjMiLCJyb2xlIjoiY2xpZW50IiwiaWF0IjoxNTA4NTI0MzYwLCJleHAiOjE1MDg1MjUyNjB9.UcGkf2nEQvBwtXy_BKTXrCehGz0BuqXmlXtf8hiiR1o', '{"username":"xx"}', ex=5)
    if response is not None:
        print('SESSION:', json.loads(response))
        return json.loads(response)
    return {}
