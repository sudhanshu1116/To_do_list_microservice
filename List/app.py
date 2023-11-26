from flask import Flask, request
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, doc = '/swagger/')

list_ns = api.namespace('List', path='/lists/', description='List')
items_ns = api.namespace('Items',path = '/item/')

list_model = api.model('Lists',{
    'id': fields.Integer(readonly=True),
    'name': fields.String(required=True),
    'description': fields.String(required=True)
} )

item_model = api.model('Items', {
    'id': fields.Integer(readonly=True),
    'list_id':fields.Integer(readonly=True),
    'item': fields.String(),
    'done': fields.Boolean()
})

class Items():

    def __init__(self):
        self.counter = 0
        self.items = []

    def get_all(self, list_id): # get all items in list
        list_items = []
        for item in self.items:
            if item['list_id'] == list_id:
                list_items.append(item)
        return list_items

    def get(self, id): # get one item
        for item in self.items:
            if item['id'] == id:
                return item
            
        api.abort(400, 'Item not found')
    
    def create(self, list_id, data): # create new Item
        item = data
        item['id'] = self.counter + 1
        item['list_id'] = list_id
        self.counter += 1
        self.items.append(item)
        return item
    
    def update(self, id, data): # update an item
        item = self.get(id)
        item.update(data)
        return item
    
    def delete_all(self, list_id):
        items = self.get_all(list_id)
        for item in items:
            self.items.remove(item)

    def delete(self, id): #delete an item
        item = self.get(id)
        self.items.remove(item)

items = Items()


class Lists():
    def __init__(self):
        self.counter = 0
        self.lists = []

    def get_all(self): # get all lists
        return self.lists

    def get(self, id): # get all items in one list
        for lst in self.lists:
            if lst['id'] == id:
                lst['items'] = items.get_all(id)
                return lst
    
    def create(self, data): # create new list
        lst = data
        lst['id'] = self.counter + 1
        self.counter += 1
        self.lists.append(lst)
        return lst
    
    def update(self, id, data): # update list
        lst = self.get(id)
        lst.update(data)
        return lst
    
    def delete(self, id): # delete list
        items.delete_all(id)
        index = 0
        for i, val in enumerate(self.lists):
            if val['id'] == id:
                index = i
                break
        self.lists.pop(index)


lists = Lists()


@list_ns.route('/')
class ListsAPI(Resource):

    @list_ns.marshal_list_with(list_model)
    def get(self):
        return lists.get_all()

    @list_ns.expect(list_model)
    def post(self):
        list_data = request.get_json()
        new_list = lists.create(list_data)
        return new_list


@list_ns.route('/<int:list_id>')
class ListAPI(Resource):
    def get(self, list_id):
        return lists.get(list_id)

    @list_ns.expect(item_model)
    def post(self, list_id):
        item_data = request.get_json()
        new_item = items.create(list_id, item_data)
        return new_item

    @list_ns.expect(list_model)
    def put(self, list_id):
        list_data = request.get_json()
        new_list = lists.update(list_id, list_data)
        return new_list

    def delete(self, list_id):
        lists.delete(list_id)


@items_ns.route('/<int:id>')
class Item(Resource):

    @list_ns.marshal_with(item_model)
    def get(self, id):
        return items.get(id)

    @list_ns.expect(item_model)
    def put(self, id):
        item_data = request.get_json()
        new_item = lists.update(id, item_data)
        return new_item

    def delete(self, id):
        items.delete(id)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug =True)