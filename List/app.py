from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

class Item():

    def __init__(self):
        self.counter = 0
        self.items = []

    def get(self):
        return self.items

    def get(self, id):
        for item in self.items:
            if item['id'] == id:
                return item
            
        api.abort(400, 'Item not found')
    
    def create(self, data):
        item = data
        item['id'] = self.counter + 1
        self.counter += 1
        self.items.append(item)
        return item
    
    def update(self, id, data):
        item = self.get(id)
        item.update(data)
        return item
    
    def delete(self, id):
        item = self.get(id)
        self.items.remove(item)




        


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug =True)