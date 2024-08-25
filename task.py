from datetime import date

class Task:
    id_counter = 0
    
    def __init__(self, name: str, desc: str = "", status: int = 0)-> None:
        
        self.id = Task.id_counter
        Task.id_counter += 1
        
        self.name = name
        self.desc = desc
        
        self.date_created = date.today()
        self.date_mod = self.date_created
        
    def update_status(self, new_status: int) -> None:
        self.status
        
    