import datetime

class Task:
    def __init__(self, name, deadline):
        self.name = name 
        self.deadline = deadline
    
    # return a string representation of the object
    def __str__(self):
        return f"{self.name} ({self.deadline})" 
    
    def update_name(self, new_name):
        self.name = new_name
    
    def update_deadline(self, new_deadline):
        self.deadline = new_deadline
               
    def delete_task(self):
        del self
    
    # class method.  Create a new task object without creating an instance
    def add_task(cls, name, deadline):
        new_task = cls(name, deadline)
        return new_task
    
class TaskManager:
    def __init__(self, tasks=None):
        self.tasks = tasks or []
        
    def display_overdue_tasks(self):
        today = datetime.date.today()
        overdue_tasks = [task for task in self.tasks if task.deadline < today]
        sorted_tasks = sorted(overdue_tasks, key=lambda task: task.deadline)
        for task in sorted_tasks:
            print(f"{task.name} ({task.deadline})")
        
        
    
    
    
        
    
            
    