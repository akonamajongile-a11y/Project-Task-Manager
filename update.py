def update():
    import csv

    task_ID = input("Please input the Task ID of the task you want to update: ")

    with open("tasks.csv", "r", newline="") as file:
        reader = csv.reader(file)

        for line in reader:
            if line[0] == task_ID:  

                task_name = input("Enter the new task name: ")

                line[1] = task_name
               
                with open("tasksnew.csv", "a", newline="") as file:
                                writer = csv.writer(file)
                                writer.writerow(line)
                print("Task updated successfully.")
            else:

                with open("tasksnew.csv", "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(line)
          
    


update()
