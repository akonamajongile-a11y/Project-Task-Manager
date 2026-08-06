def add_tasks():
    import csv 
    count = -1 
    with open("task.csv", "r", newline="") as file: 
                reader =csv.reader(file)
                for e in reader: 
<<<<<<< HEAD
                       count = count + 1 
    task_ID = count + 1
    valid_name = False
    while not valid_name:
        task_name = input("Please input your task name:").capitalize().strip()
        if task_name == "":
                valid_name = False
                print("This is a required field.")
        else: 
                valid_name = True  
    valid_category = False
    while not valid_category:           
        category = input("Please select the category (Work/Personal):").capitalize().strip()
        if category == "Work":
               print("You have made a selection: Work ")
        elif category == "Personal":
               print("You have a made seletion: Personal")
        else: 
               print("You have made an incorrect selection")
        if category == "":
               valid_category = False
               print("This is a required field.") 
        else: 
               valid_category = True 
    valid_description = False
    while not valid_description: 
        description = input("Please enter the description of the task: ").capitalize().strip()
        if description == "" :
               valid_description = False
               print("This is a required field.")
        else: 
               valid_description = True
    valid = False
    while not valid:
        priority = input("Please select the priority level (Low/Medium/High): ").capitalize().strip()
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
    try: 
           if len(due_date) != 10:
                  raise ValueError("Incorrect format length")
           date_obj = datetime.strptime(due_date, "%d/%m/%Y")
           print("Valid date: ", date_obj)
    except ValueError as e: 
           print("Error: ", e)
    valid_status = False
    while not valid_status:
        status = input("Please select a status level (Not started/ Started/ Done): ").capitalize().strip()
        if status == "Not started": 
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
                print("Please insert correct status option!")

=======
                       count =  count + 1 

    task_ID = count + 1
    task_name = input("Please input your tasks name:").capitalize()
    task_description = input("Please enter the description of the task: ").capitalize()
    task_due_date = input("The due date of the task is (DD/MM/YYY): ")
    task_priority = input("Please select the priority level (Low/MediumHigh): ").capitalize()
    task_category = input("Please select the category (Personal/business)")
>>>>>>> 5e39284666a11b9b53a776afa893aeb5ed94c631
    import csv 
    with open("tasks.csv", "a", newline="") as file: 
<<<<<<< HEAD
            writer =csv.writer(file)    
            writer.writerows([[task_ID, task_name, description, due_date, priority, category, status]])
=======
            writer =csv.writer(file)
            writer.writerows([[task_ID, task_name, task_description, task_due_date, task_priority, task_category]])

    print("CSV successfully created")







>>>>>>> 5e39284666a11b9b53a776afa893aeb5ed94c631
