import datetime
import tkinter as tk

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
        
    def display_all_tasks(self):
        for task in self.tasks:
            print(task)
     
     # sort the overdue tasks and print them   
    def display_overdue_tasks(self):
        today = datetime.date.today()
        overdue_tasks = [task for task in self.tasks if task.deadline < today]
        sorted_tasks = sorted(overdue_tasks, key=lambda task: task.deadline)
        for task in sorted_tasks:
            print(f"{task.name} ({task.deadline})")
        
task_manager = TaskManager()

task1 = Task("Finish project", datetime.date(2023, 2, 28))
task2 = Task("Complete CSS Project", datetime.date(2023, 4, 15))
task3 = Task("Submit proposal", datetime.date(2022, 5, 10))
task4 = Task("Update website content", datetime.date(2022, 7, 1))
task5 = Task("Prepare for presentation", datetime.date(2024, 8, 15))

task_manager.tasks.append(task1)
task_manager.tasks.append(task2)
task_manager.tasks.append(task3)
task_manager.tasks.append(task4)
task_manager.tasks.append(task5)

task_manager.display_all_tasks()

print()

print("Here is a list of the overdue tasks")
task_manager.display_overdue_tasks()
      
    
    
    
        
    
            
    