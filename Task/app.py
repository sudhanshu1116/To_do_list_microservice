from flask import Flask , request
from flask_restx import Api, Resource, fields

app=Flask(__name__)
api=Api(app,doc='/swagger/')

#Renamed namespace to tasks
task_ns=api.namespace('task',path='/tasks/',description='Task')

#renamed to task, item-->taskname, added description👍
Item_model=api.model('task',{
    'id':fields.Integer(readonly=True,description='id'),
    'taskname': fields.String(required=True, description="The Item to be completed"),
    'description': fields.String(required=True, description="Short description of task"),
    'done': fields.Boolean(reqired=True,description="Item Completed or not"),
    'Start_time': fields.String(reqired=True,description="Start Time"),
    'End_time':fields.String(reqired=True,description="End Time")
})

class task_Items():
    def __init__(self):
        self.counter=0
        self.Task=[]
    def get_all(self):
        return self.Task
    def get(self,id):
        for Task in self.Task:
            if Task['id']==id:
                return Task
        api.abort(400,'Task not Found')
    def create(self,data):
        Task=data
        Task['id']=self.counter+1
        self.counter+=1
        self.Task.append(Task)
        return Task
    def update(self,id,data):
        Task=self.get(id)
        Task.update(data)
        return Task
    def delete(self,id):
        Task=self.get(id)
        self.Task.remove(Task)
Task=task_Items()

if __name__ =='__main__':
    app.run(host='127.0.0.1',port=5001, debug=True)


