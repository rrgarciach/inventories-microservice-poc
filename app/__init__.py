from flask import Flask, request, jsonify, redis
import logging

def request_wants_json():
    best = request.accept_mimetypes \
        .best_match(['application/json', 'text/html'])
    return best == 'application/json' and \
        request.accept_mimetypes[best] > \
        request.accept_mimetypes['text/html']

def create_app():
    @app.route('/api/v1/orders', methods=['GET'])
    def getAllOrders():
        r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        response = r.get('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiJmb28xMjMiLCJyb2xlIjoiY2xpZW50IiwiaWF0IjoxNTA4NDY0MTUyLCJleHAiOjE1MDg0NjUwNTJ9.0mR9thJ1pN43vOt0XK92VJVISOCadgFQOn90FIw40d4')
        if request_wants_json():
            # return jsonify({"message": 'hello!'})
            return response
        return 'not json'
