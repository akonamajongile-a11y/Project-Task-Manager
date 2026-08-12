import csv

def task_dashboard():
    dash_categories = ""
    total_tasks = 0
    completed_tasks = 0
    overdue_tasks = 0 
    pending_tasks = 0
    work_tasks = 0
    personal_tasks = 0
    category_tasks = 0

    

    from datetime import datetime
    today = datetime.today().date()  # current date
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
            elif everything[6] == "Pending":
                pending_tasks +=1
              

            # Count overdue tasks: Pending & due date is before today
            if  due_date < today:
                overdue_tasks +=1

    with open("tasks.csv" , "r" , newline="") as file:
        reader = csv.reader(file)

        for everything in reader:
            status = everything[2].lower()

           # Count Tasks per Category:
           # Count Work Tasks:
            if everything[2] == "Work":
               work_tasks +=1
           
            # Count Personal Tasks:
            elif everything[2] == "Personal":
                personal_tasks +=1  

            # Calculate percentages
    if total_tasks > 0:
        completed_percentage = (completed_tasks / total_tasks) * 100
        overdue_percentage = (overdue_tasks / total_tasks) * 100
        pending_percentage = (pending_tasks / total_tasks) * 100

        work_percentage = (work_tasks / total_tasks) * 100
        personal_percentage = (personal_tasks / total_tasks) * 100    


            # Print no. of tasks
    print("=====================================")
    print(" " * 11 + "Task Dashboard")
    print("====================================")
    print(f"Total Tasks: {total_tasks}")
    print(f"Completed Tasks: {completed_tasks}")
    print(f"Incomplete Tasks: {pending_tasks}")
    print("====================================")
    print(f"Overdue Tasks: {overdue_tasks} ({overdue_percentage:.2f}%)")
    print("====================================")
    print(f"Work Tasks: {work_tasks}")
    print(f"Personal Tasks: {personal_tasks}")
    print("====================================")

           # Print Distribution of tasks
    print(f"Distribution Of Tasks Per Status:")
    print(f"% of Completed Tasks: ({completed_percentage:.2f}%)")
    print(f"% of Incomplete Tasks: ({pending_percentage:.2f}%)")
    print("====================================")
    print(f"Distribution Of Tasks Per Category:")
    print(f"% of Work Tasks: ({work_percentage:.2f}%)")
    print(f"% of Personal Tasks: ({personal_percentage:.2f}%)")
    print("====================================")
    print("Keep going, you’re doing great :)")

    

