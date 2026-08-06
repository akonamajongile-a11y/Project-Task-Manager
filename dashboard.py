def task_dashboard():
 import csv
 from colorama import Fore, Style
 with open("tasks.csv" , "r" , newline="") as file:
    reader = csv.reader(file)
  
dash_categories = "total_tasks" == 0
"completed_tasks" == 0
"overdue_tasks" == 0 

#dash_categories["total_tasks"] += 1
#dash_categories["completed_tasks"] += 1
#dash_categories["overdue_tasks"] += 1

from datetime import datetime
today = datetime.today().date()  # current date

import csv
from colorama import Fore, Style
with open("tasks.csv" , "r" , newline="") as file:
    reader = csv.reader(file)

for everything in reader:
    total_tasks += 1
    status = everything[6].lower() 
    due_date = datetime.strptime(everything[5], "%Y-%m-%d").date()

    # Count completed tasks
    if status == "done":
                completed_tasks += 1

    # Count overdue tasks (not done AND due date before today)
    if status != "done" and due_date < today:
        overdue_tasks += 1

#"total_tasks" == 0
#"completed_tasks" == 0
#"overdue_tasks" == 0

print("Task Dashboard")
print("==========================")
print(f"Total Tasks: {'total_tasks'}")
print(f"Completed Tasks: {'completed_tasks'}")
print(f"Overdue Tasks: {'overdue_tasks'}")
print("==========================")
print("Keep going, you’re doing great!")




 
task_dashboard()