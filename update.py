def update():
    import csv

    task_ID = input("Please input the Task ID of the task you want to update: ")

    with open("tasks.csv", "r", newline="") as file:
        reader = csv.reader(file)

        for line in reader:
            if line[0] == task_ID:  
                option = input(""" 
    1. Task Name
    2. Category: Work/Personal
    3. Description
    4. Priority: High/Medium/Low
    5. Due Date
    6. Status: Not Started/Started/Done
    Choose the option you what to update? : """)

                
                if option == "1":
                    task_name = input("Enter the new task name: ")
                    line[1] = task_name
                elif option == "2":
                    category = input("Enter the new category: ")
                    line[2] = category
                elif option == "3":
                    description = input("Enter the new description: ")
                    line[3] = description 
                elif option == "4":
                    priority = input("Enter the new priority: ")
                    line[4] = priority 
                elif option == "5":
                    due_date = input("Enter the new due_date: ")
                    line[5] = due_date 
                elif option == "6":
                    status = input("Enter the new status : ")
                    line[6] = status  
                else:
                    print("Please enter a valid option! ") 
              
               
                with open("tasksnew.csv", "a", newline="") as file:
                   writer = csv.writer(file)
                   writer.writerow(line)
                   print("Task updated successfully.")

            else:

                with open("tasksnew.csv", "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(line)
          

