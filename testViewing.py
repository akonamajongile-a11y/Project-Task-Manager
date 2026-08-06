#import add_feature
#import update
#import deletion
import viewing

def task():
 print("Welcome to Task Manager")
 print("To continue, select an option below")
 print("1: Add Task")
 print("2: Update Task")
 print("3: Delete Task")
 print("4: View Task")
 print("5: Search Task")
 
 option = input("Please select your option")
 
 if option == '4':
     viewing.view_task()
     # if option == '2':
     #     update.edit_task()
     # if option == '3':
     #     deletion.delete_task()
     # # if option == '4':
     # #   viewing.view_task()
task()