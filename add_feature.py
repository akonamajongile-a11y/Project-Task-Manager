def add_tasks():
    import csv 
    count = 0
    with open("tasks.csv", "r", newline="") as file: 
                reader =csv.reader(file)

                for e in reader: 
                       count = count + 1 

    task_ID = count + 1
    task_name = input("Please input your tasks name:").capitalize()
    category = input("Please select the category (Work/Personal)").capitalize()
    description = input("Please enter the description of the task: ").capitalize()
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

    due_date = input("The due date of the task is (DD/MM/YYY): ")
    import datetime 
    due_date = datetime.datetime.now()
    print(due_date.year)
    print(due_date.strftime("%A"))

    status = input("Please select a status level (Not Started/ Started/ Done): ").capitalize()
    import csv 

    with open("tasks.csv", "a", newline="") as file: 
            writer =csv.writer(file)
            writer.writerows([[task_ID, task_name, description, due_date, priority, category, status]])
