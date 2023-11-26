from flask import Flask, request
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

list_ns = api.namespace('List', path='items', description='To Do List')


class Items():

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

items = Items()



list_ns.route('/')
class ItemsAPI(Resource):

    def get(self):
        return items.get()

    def post(self):
        data = request.get_json()
        new_item = items.create(data)
        return new_item


list_ns.route('/<int:id>')
class ItemAPI(Resource):

    def get(self, id):
        return items.get(id)

    def put(self, id):
        data = request.get_json()
        updated_item = items.update(id,data)
        return updated_item

    def delete(self, id):
        items.delete(id)
        return {'Message': 'Successfully deleted'}


if __name__ == '__main__':
    app.run(debug =True)