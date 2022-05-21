from flask import Flask, request, jsonify
from flask_restx import Api, Resource

from src.server.instance import server


app, api = server.app, server.api

from src.services.addDevService import addDev


@api.route('/devs', methods=['GET', 'POST'])

class DevController(Resource):
    def get(self, ):
        return

    def post(self, ):
        data = request.json
        addDev.execute(data)
        


