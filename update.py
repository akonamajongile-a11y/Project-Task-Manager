from datetime import datetime


def update():
    import csv

    task_ID = input("Please input the Task ID of the task you want to update: ")
    rows = [] 
    found = False # List to store all rows
    with open("tasks.csv", "r", newline="") as file:
        reader = csv.reader(file)

        for line in reader:
            if line[0] == task_ID:
                found = True

                option = input("""
1. Task Name
2. Category: Work/Personal
3. Description
4. Priority: High/Medium/Low
5. Due Date
6. Status: Pending/Done
Choose the field you want to update (1-6): """)

                valid_options = ["1", "2", "3", "4", "5", "6"]

                if option == "1":
                    task_name = input("Enter the new task name: ").capitalize().strip()
                    while task_name == "":
                        print("This is a required field, please enter a valid task name.")
                        task_name = input("Enter the new task name: ").capitalize().strip()
                    line[1] = task_name

                elif option == "2":
                    category = input("Enter the new category (Work/Personal): ").capitalize().strip()

                    while category not in ["Work", "Personal"]:
                        print("Please enter Work or Personal.")
                        category = input("Enter the new category (Work/Personal): ").capitalize().strip()
                    line[2] = category

                elif option == "3":
                    description = input("Enter the new description: ").strip()
                    while description == "":
                        print("Description cannot be empty.")
                        description = input("Enter the new description: ").strip()
                    line[3] = description

                elif option == "4":
                    priority = input("Enter the new priority (High/Medium/Low): ").capitalize().strip()
                    while priority not in ["High", "Medium", "Low"]:
                        print("Please enter High, Medium, or Low.")
                        priority = input("Enter the new priority (High/Medium/Low): ").capitalize().strip()
                    line[4] = priority

                elif option == "5":
                    while True:
                        due_date = input("Enter the new due date (DD/MM/YYYY): ").strip()

                        try:
                            datetime.strptime(due_date, "%d/%m/%Y")
                            line[5] = due_date
                            break
                        except ValueError:
                          print("Please enter the date in DD/MM/YYYY format.")
                         

                elif option == "6":
                    status = input("Enter the new status (Pending/Done): ").title().strip()
                    while status not in ["Pending", "Done"]:
                        print("Which status are you updating (Pending/Done)? ")
                        status = input("Enter the new status (Pending/Done): ").title().strip()
                    line[6] = status
                else:
                    while option not in valid_options:
                        print("Please enter a valid option!")
                        option = input("Choose the field you want to update (1-6): ")
    
            rows.append(line)

        if not found:
         print("Task ID not found!")
         return

        with open("tasks.csv", "w", newline="") as file:
         writer = csv.writer(file)
         writer.writerows(rows)
         print("Task updated successfully!")

#update()