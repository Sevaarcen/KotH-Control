import toml
import base64

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = Api(app)

class LocalFile(Resource):
    def get(self, resource_name):
        if resource_name not in local_files:
            abort(404)
        local_file_path = local_files.get(resource_name)
        file = open(local_file_path, 'rb')
        b64data = base64.b64encode(file.read())
        return b64data.decode('utf-8')

class LocalFileList(Resource):
    def get(self):
        return local_files

class Host(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()
        print(repr(args))
        return args

api.add_resource(Host, '/')
api.add_resource(LocalFileList, '/getfile/')
api.add_resource(LocalFile, '/getfile/<resource_name>')

if __name__ == "__main__":
    config = toml.load('config.toml')
    local_files = config.setdefault('api', {}).get('exposed-files', {})
    app.run(debug=True)