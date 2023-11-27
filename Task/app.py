from flask import Flask , request
from flask_restx import Api, Resource, fields

app=Flask(__name__)
api=Api(app,doc='/swagger/')
task_ns=api.namespace('list',path='/items/',description='List')
item_model=api.model('item',{
    'id':fields.Integer(readonly=True,description='id'),
    'item': fields.String(required=True, description="The Item to be completed"),
    'done': fields.Boolean(reqired=True,description="Item Completed or not"),
    'Start_time': fields.Boolean(reqired=True,description="Start Time"),
    'End_time':fields.Boolean(reqired=True,description="End Time")
})
