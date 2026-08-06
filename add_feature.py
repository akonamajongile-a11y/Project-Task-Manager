def add_tasks():
    import csv 
    count = -1 
    with open("tasks.csv", "r", newline="") as file: 
                reader =csv.reader(file)
                for e in reader: 
                       count =  count + 1 

    task_ID = count + 1
    task_name = input("Please input your tasks name:").capitalize()
    task_description = input("Please enter the description of the task: ").capitalize()
    task_due_date = input("The due date of the task is (DD/MM/YYY): ")
    task_priority = input("Please select the priority level (Low/MediumHigh): ").capitalize()
    task_category = input("Please select the category (Personal/business)")
    import csv 
    with open("tasks.csv", "a", newline="") as file: 
            writer =csv.writer(file)
            writer.writerows([[task_ID, task_name, task_description, task_due_date, task_priority, task_category]])

    print("CSV successfully created")







