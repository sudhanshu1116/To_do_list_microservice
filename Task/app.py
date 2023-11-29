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

class TaskItems():

    def __init__(self):
        self.counter=0
        self.tasks=[]

    def get_all(self):
        return self.tasks
    
    def get(self,id):
        for task in self.tasks:
            if task['id']==id:
                return task
        api.abort(400,'Task not Found')

    def create(self,data):
        task=data
        task['id']=self.counter+1
        self.counter+=1
        self.tasks.append(task)
        return task
    
    def update(self,id,data):
        task=self.get(id)
        task.update(data)
        return task
    
    def delete(self,id):
        task=self.get(id)
        self.task.remove(task)

task=TaskItems()
@task_ns.route('/')
class TasksAPI(Resource):
    @task_ns.marshal_list_with(Item_model)
    def get(self):
        return TaskItems.get_all()
    
    @task_ns.expect(Item_model)
    def post(self):
        data =request.get_json()
        new_task=TaskItems.create(data)
        return new_task
    
@task_ns.route('/<int:id>')
class TaskAPI(Resource):
    @task_ns.marshal_with(Item_model)
    def get(self,id):
        return task.get(id)
    @task_ns.expect(Item_model)
    def get(self,id):
        data =request.get_json()
        updated_task=TaskItems.update(id,data)
        return task.get(id)
    def delete(self,id):
        TaskItems.delete(id)
        return{'Message':'Successfully deleted'}

if __name__ =='__main__':
    app.run(host='127.0.0.1',port=5001, debug=True)


