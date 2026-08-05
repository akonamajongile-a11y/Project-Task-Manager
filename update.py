def update():
    import csv

    task_ID = input("Please input the Task ID of the task you want to update: ")

    with open("tasks.csv", "r", newline="") as file:
        reader = csv.reader(file)

        for e in reader:
            if e[0] == task_ID:  
                print("Task found:",e)

            task_name = input("Enter the new task name: ")

            e[1] = task_name
            found = True
            e.append(e)

        if found:

         with open("tasks.csv", "w", newline="") as file:
          writer = csv.writer(file)
          writer(e)
         print("Task updated successfully.")
        else:
           print("Task ID not found.")


update()
