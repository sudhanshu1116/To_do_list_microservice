from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

class Items():

    def __init__(self):
        self.counter = 0
        self.items = []

    

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port=5000, debug=True)