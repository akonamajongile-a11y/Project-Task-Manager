def task_dashboard():
    dash_categories = ""
    total_tasks = 0
    completed_tasks = 0
    overdue_tasks = 0 
    pending_tasks = 0

    

    from datetime import datetime
    today = datetime.today().date()  # current date
    import csv
    with open("tasks.csv" , "r" , newline="") as file:
        reader = csv.reader(file)

            # Count Total Tasks
        for everything in reader:
            total_tasks += 1
            status = everything[6].lower() 
            due_date = datetime.strptime(everything[5], "%d/%m/%Y").date()
        
            # Count Completed Tasks: "Done"
            if everything[6] == "Done":
                completed_tasks += 1

                #Count Pending Tasks: "Pending"
            elif everything[6] == "Pending" and due_date > today:
                pending_tasks +=1
              

            # Count overdue tasks: Pending & due date is before today
            else:
                everything[6] == "Pending" and due_date < today
                overdue_tasks +=1
                

    print("=====================================")
    print(" " * 11 + "Task Dashboard")
    print("=====================================")
    print(f"Total Tasks: {total_tasks}")
    print(f"Completed Tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Overdue Tasks: {overdue_tasks}")
    print("=====================================")
   

# Calculate percentages
    if total_tasks > 0:
        completed_percentage = (completed_tasks / total_tasks) * 100
        overdue_percentage = (overdue_tasks / total_tasks) * 100
        pending_percentage = (pending_tasks / total_tasks) * 100

    print(f"Distribution Of Tasks Per Status:")
    print(f"% of Completed tasks: ({completed_percentage:.2f}%)")
    print(f"% of Pending tasks: ({pending_percentage:.2f}%)")
    print(f"% of Overdue tasks: ({overdue_percentage:.2f}%)")
    print("====================================")

    print("Keep going, you’re doing great!")

