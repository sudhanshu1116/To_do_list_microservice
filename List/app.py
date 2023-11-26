from flask import Flask, request
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, doc = '/swagger/')

list_ns = api.namespace('List', path='/items/', description='List')

item_model = api.model('Item', {
    'id': fields.Integer(readonly=True, description='id'),
    'item': fields.String(required=True, description = "The item to be completed"),
    'done': fields.Boolean(required=True, description="Item completed or not")
})

class Items():

    def __init__(self):
        self.counter = 0
        self.items = []

    def get_all(self):
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



@list_ns.route('/')
class ItemsAPI(Resource):

    @list_ns.marshal_list_with(item_model)
    def get(self):
        return items.get_all()

    @list_ns.expect(item_model)
    def post(self):
        data = request.get_json()
        new_item = items.create(data)
        return new_item


@list_ns.route('/<int:id>')
class ItemAPI(Resource):

    @list_ns.marshal_with(item_model)
    def get(self, id):
        return items.get(id)

    @list_ns.expect(item_model)
    def put(self, id):
        data = request.get_json()
        updated_item = items.update(id,data)
        return updated_item

    def delete(self, id):
        items.delete(id)
        return {'Message': 'Successfully deleted'}


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug =True)