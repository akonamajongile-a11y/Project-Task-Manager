import add_feature as ad
import update 
import deletion as delete
import viewing as view
import search 
import notifications as nt
import dashboard as db
import csv 
from datetime import datetime 

print("Welcome to Task Manager")
print("Top 5 tasks for the day")
def get_top_tasks():
            with open("tasks.csv", "r", newline="") as file: 
                reader = csv.reader(file)
    
                for e in reader:
                    task_id = e[0]
                    today = datetime.now().date()
                    due_date = datetime.strptime(e[5], "%d/%m/%Y").date()
                    if due_date == today:
                         print(e)
get_top_tasks()
def task():
    print("To continue, select an option below")
    print("1: Add Task")
    print("2: Update Task")
    print("3: Delete Task")
    print("4: View Task")
    print("5: Search Task")
    print("6: View your Dashboard")
    print("7 See Notifiations")

    option = input("Please select your option")

    if option == '1':
        ad.add_tasks()
    elif option == '2':
        update.update()
    elif option == '3':
        delete.task_deletion()
    elif option == '4':
        view.view_task()

    elif option == '5':
        search.search_engine()

    elif option == '6':
        db.task_dashboard()

    elif option == '7':
        nt.notifications()

    else:
        print("Please insert a correct option!")


task()
    