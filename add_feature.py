def add_tasks():
    import csv 
    count = 0
    with open("tasks.csv", "r", newline="") as file: 
                reader =csv.reader(file)

                for e in reader: 
                       count = count + 1 

    task_ID = count + 1
    task_name = input("Please input your tasks name:").capitalize()
    task_category = input("Please select the category (Work/Personal)").capitalize()
    task_description = input("Please enter the description of the task: ").capitalize()
    valid = False
    while not valid:
        task_priority = input("Please select the priority level (Low/Medium/High): ").capitalize()
        if task_priority == "Low": 
                    valid = True
                    print("You have selected: Low" )
        elif task_priority == "Medium":
                valid = True
                print("You have selected: Medium")
        elif task_priority == "High":
                valid = True
                print("You have selected: High")
        else:
            print("Please insert correct priority option!")

    task_due_date = input("The due date of the task is (DD/MM/YYY): ")
    import datetime 
    task_due_date = datetime.datetime.now()
    print(task_due_date.year)
    print(task_due_date.strftime("%A"))

    task_status = input("Please select a status level (Not Started/ Started/ Done): ").capitalize()
    import csv 

    with open("tasks.csv", "a", newline="") as file: 
            writer =csv.writer(file)
            writer.writerows([[task_ID, task_name, task_description, task_due_date, task_priority, task_category,task_status]])
add_tasks()