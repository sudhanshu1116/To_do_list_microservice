from flask import Flask , request
from flask_restx import Api, Resource, fields

app=Flask(__name__)
api=Api(app,doc='/swagger/')

#Renamed namespace to tasks
task_ns=api.namespace('task',path='/tasks/',description='Task')

#renamed to task, item-->taskname, added description
item_model=api.model('task',{
    'id':fields.Integer(readonly=True,description='id'),
    'taskname': fields.String(required=True, description="The Item to be completed"),
    'description': fields.String(required=True, description="Short description of task"),
    'done': fields.Boolean(reqired=True,description="Item Completed or not"),
    'Start_time': fields.String(reqired=True,description="Start Time"),
    'End_time':fields.String(reqired=True,description="End Time")
})
