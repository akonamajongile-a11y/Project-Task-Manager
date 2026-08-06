def add_tasks():
    import csv 
    count = 0
    with open("tasks.csv", "r", newline="") as file: 
                reader =csv.reader(file)

                for e in reader: 
                       count = count + 1 
    task_ID = count + 1

    valid_name = False
    while not valid_name:
        task_name = input("Please input your tasks name:").capitalize()
        if task_name == "":
                valid_name = False
                print("The user is required to input a task name")
        else: 
                valid_name = True  
    valid_category = False

    while not valid_category:           
        category = input("Please select the category (Work/Personal)").capitalize()
        if category == "":
               valid_category = False
               print("The user is required to input a category") 
        else: 
               valid_category = True 

    valid_description = False
    while not valid_description: 
        description = input("Please enter the description of the task: ").capitalize()
        if description == "" :
               valid_description = False
               print("The user is required to input a description")
        else: 
               valid_description = True
               
    valid = False
    while not valid:
        priority = input("Please select the priority level (Low/Medium/High): ").capitalize()
        if priority == "Low": 
                    valid = True
                    print("You have selected: Low" )
        elif priority == "Medium":
                valid = True
                print("You have selected: Medium")
        elif priority == "High":
                valid = True
                print("You have selected: High")
        else:
            print("Please insert correct priority option!")

    
    from datetime import datetime 
    due_date = input("The due date of the task is (DD/MM/YYY): ")  
    valid_status = False
    while not valid_status:
        status = input("Please select a status level (Not started/ Started/ Done): ").capitalize()
        if status == "Not Started": 
                valid_status = True
                print("You have selected: Not started" )
                print("CSV Sucessfully created")
        elif status == "Started":
                valid_status = True
                print("You have selected: Started ")
                print("CSV Sucessfully created")
        elif status == "Done":
                valid_status = True
                print("You have selected: Done ")
                print("CSV Sucessfully created")
        else:
                print("Please insert correct priority option!")
    import csv 

    with open("tasks.csv", "a", newline="") as file: 
            writer =csv.writer(file)
            writer.writerows([[task_ID, task_name, description, due_date, priority, category, status]])

add_tasks()