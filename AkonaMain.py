import add_feature
import update
import deletion
import viewing
import search
import notifications
import dashboard

def task():
    print("Welcome to Task Manager")
    print("Top 5 tasks for the day")

    
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
        add_feature.add_tasks()
    elif option == '2':
        update.update()
    elif option == '3':
        deletion.task_deletion()
    elif option == '4':
        viewing.view_task()

    elif option == '5':
        search.search_engine()

    elif option == '6':
        dashboard.task_dashboard()

    elif option == '7':
        notifications.notifications()

    else:
        print("Please insert a correct option!")


task()
    