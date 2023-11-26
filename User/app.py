from flask import Flask, request
from flask_restx import Resource, Api


app = Flask(__name__)
api = Api(app)

# @app.route('/')
# def hello():
#     return '<h1>Hello</h1>'

users = [{
    'id': 0,
    'username': 'Manasvi',
    'pwd': 'Idiot'
},
{
    'id': 1,
    'username': 'Sudhnashu',
    'pwd': 'Stupid'
}]


@api.route('/users')
class Users(Resource):

    def get(self):
        return users
    
@api.route('/user/<int:id>')
class User(Resource):

    def get(self,id):
        return users[id]
    
    def post(self, id):
        args = request.get_json()
        users.append(args)
        return {'message': 'Successful'}
    
    def put(self,id):
        args = request.get_json()
        users[args['id']] = args
        return {'message': 'successful'}





if __name__ == "__main__":
    app.run(host= '127.0.0.', port= 8008, debug= True)