def notifications(): 
        import csv 
        count = 0
        with open("tasks.csv", "r", newline="") as file: 
                reader =csv.reader(file)
                for e in reader: 
                       count = count + 1
                       print(" ======== TASK NOTIFICATIONS ========")
        from datetime import datetime 
        today = "07/08/2026"
        due_date = False
        while not due_date: 
                due_date = input("The due date of the task is (DD/MM/YYY): ")
                if due_date > today:
                        print("You are overdue with your tasks")
                else:
                        if due_date < str(14):
                                print("Please note that your task is close to the due date")





























notifications()


                
    