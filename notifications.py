import csv 
from datetime import datetime 
def notifications(): 
       
        
        today = datetime.today().date()
        
        with open("tasks.csv", "r", newline="") as file: 
            reader = csv.reader(file)

            for e in reader:
                task_id = e[0]
                today = datetime.now().date()
                due_date = datetime.strptime(e[5], "%d/%m/%Y").date()
                days_left = (due_date - today).days
                if days_left < 0:
                    print("Task ID", task_id, "is overdue")
                elif days_left <= 2:
                    print("Task ID", task_id, "is close to the due date")

       