def view_task():
    import csv
    with open("tasks.csv" , "r" , newline="") as file:
        reader = csv.reader(file)

        print("Task ID: " + "Task Name: " + "Category: " + "Description: " + "Priority: " + "Due Date: " + "Status: ")
        for everything in reader:
            print(everything)


