import add_feature


def task():
 print("Welcome to Task Manager")
 print("To continue, select an option below")
 print("1: Add Task")
 print("2: Update Task")
 print("3: Delete Task")
 # print("4: View Task")
 print("5: Search Task")

 option = input("Please select your option")

 if option == '1':
    add_feature.add_tasks()
task()