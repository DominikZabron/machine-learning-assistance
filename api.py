from flask import Flask
from flask_restful import Resource, Api, reqparse, inputs

app = Flask(__name__)
api = Api(app)

class Text(Resource):
    def post(self):
        return '', 204

class Images(Resource):
    def post(self):
        return '', 204


api.add_resource(Text, '/text')
api.add_resource(Images, '/images')


if __name__ == "__main__":
    app.run(debug=True)
