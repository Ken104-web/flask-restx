from flask_restx import Resource,  Namespace

ns = Namespace("home")

@ns.route("/hello")
class Greet(Resource):
    def get(self):
        return {"Hello": "it's working"}

