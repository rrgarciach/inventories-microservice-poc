import session

from flask import Flask, request, jsonify

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
    userSession = session.getSession('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiJmb28xMjMiLCJyb2xlIjoiY2xpZW50IiwiaWF0IjoxNTA4NTMwNTg2LCJleHAiOjE1MDg1MzE0ODZ9.0ydDCd5nRSdrWwfZSLXk3_zFBa9igkv9bmqok9l-GtU')
    return userSession
