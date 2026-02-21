import json
from task import Task

class TaskManager:
    def __init__(self):
        self.tasks= []
        self.filename = "tasks.json"
        self.load_tasks()

    def add_task(self, title):
        new_id = len(self.tasks) + 1
        task = Task(new_id, title)
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