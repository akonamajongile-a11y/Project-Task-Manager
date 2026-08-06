
def view_task():
    import csv
    with open("tasks.csv" , "r" , newline="") as file:
        reader = csv.reader(file)
        task_categories = "Task ID:       " + "Task Name:      " + "Category:      " + "Description:     " + "Priority:     " + "Due Date:      " + "Status:      "
        print(task_categories)
        for everything in reader:
            print(everything[0]   + everything[1]   + everything[2]   + everything[3]   + everything[4]   + everything[5]) 
    print("Keep going, you're doing great!")
       
