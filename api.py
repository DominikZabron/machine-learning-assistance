from flask import Flask, request
from flask_restful import Resource, Api, reqparse, inputs
from celery.result import AsyncResult

from tasks import get_text, get_images, celery_app

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('site')

class Text(Resource):
    def post(self):
        args = parser.parse_args()
        result = get_text.delay(args['site'])
        return {'task_id': result.task_id}

class Images(Resource):
    def post(self):
        args = parser.parse_args()
        result = get_images.delay(args['site'])
        return {'task_id': result.task_id}

class Status(Resource):
    def get(self, task_id):
        status = AsyncResult(task_id, app=celery_app).status
        return {'status': status}


api.add_resource(Text, '/text')
api.add_resource(Images, '/images')
api.add_resource(Status, '/status/<task_id>')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
