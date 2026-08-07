import add_feature
import update
import deletion
import viewing
import search

def task():
    print("Welcome to Task Manager")
    print("To continue, select an option below")
    print("1: Add Task")
    print("2: Update Task")
    print("3: Delete Task")
    print("4: View Task")
    print("5: Search Task")

    option = input("Please select your option")

    if option == '1':
        add_feature.add_tasks()
    elif option == '2':
        update.update()
    elif option == '3':
        deletion.task_deletion()
    elif option == '4':
        viewing.view_task()

    elif option == '5':
        search.search_engine()

    else:
        print("Please insert a correct option!")


task()
    