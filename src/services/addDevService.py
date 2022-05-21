from src.server.database.mongoConnection  import mongodb


mongodb.initialize()

class AddDevService():
    def execute(self, data):

        mongodb.insert("devs", data)


addDev = AddDevService()
