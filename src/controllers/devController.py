from flask import Flask
from flask_restx import Api, Resource

from src.server.instance import server

app, api = server.app, server.api

devs_db = [
    {'id' : 0, 'title': 'NodeJs'},
    {'id' : 1, 'title': 'Typescript'}

]

@api.route('/devs')
class DevController(Resource):
    def get(self, ):
        return devs_db

    def post(self,):
        return devs_db

