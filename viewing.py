def view_task():
    import csv
    with open("tasks.csv" , "r" , "newlines") as file:
        reader = csv.reader(file)

        for everything in reader:
            print("Task Name: " + "Category: " + "Description: " + "Priority: " + "Due Date: " + "Status: ")
            