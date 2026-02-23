import json
import uuid
from task import Task

class TaskManager:
    def __init__(self):
        self.tasks= []
        self.filename = "tasks.json"
        self.load_tasks()

    def add_task(self, title, priority, deadline):
        new_id = str(uuid.uuid4())
        task = Task(new_id, title, priority=priority, deadline=deadline)
        self.tasks.append(task)
        self.save_tasks()
    
    def get_tasks(self):
        return self.tasks
    
    def mark_done_by_id(self, id):
        for task in self.tasks:
            if task.id == id:
                task.mark_done()
        self.save_tasks()
    
    def delete_done(self):
        new_list = []

        for task in self.tasks:
            if task.done == False:
                new_list.append(task)
        self.tasks = new_list
        self.save_tasks()
        

    def save_tasks(self):
        data = []
        for task in self.tasks:
            data.append(task.to_dict())

        with open(self.filename, "w") as f:
            json.dump(data, f)

    def load_tasks(self):
        try:
            with open(self.filename, "r") as f:

                data = json.load(f)

            for item in data:
                task = Task.from_dict(item)
                self.tasks.append(task)
            
        except FileNotFoundError:
            self.tasks = []

        except json.JSONDecodeError:
            self.tasks = []
    
    def get_task_by_id(self, id):
        for task in self.tasks:
            if task.id == id:
                return task
            
    def edit_task(self, id, title, priority, deadline):
        for task in self.tasks:
            if task.id == id:
                task.title = title
                task.priority = priority
                task.deadline = deadline
        self.save_tasks()

    def get_tasks_by_priority(self, priority):
        new_list = []

        for task in self.tasks:
            if task.priority == priority:
                 new_list.append(task)
        return new_list  