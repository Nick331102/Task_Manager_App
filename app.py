class Task:
    def __init__(self, name, deadline):
        self.name = name 
        self.deadline = deadline
    
    def __str__(self):
        return f"{self.name} ({self.deadline})" 
    
    def update_name(self, new_name):
        self.name = new_name
    
    def update_deadline(self, new_deadline):
        self.deadline = new_deadline
               
    def delete_task(self):
        del self
    
    def add_task(cls, name, deadline):
        new_task = cls(name, deadline)
        return new_task
        
            
    