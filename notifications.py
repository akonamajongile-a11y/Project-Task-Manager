def notifications(): 
        from datetime import datetime 
        print(" ======== TASK NOTIFICATIONS ========")
        today = datetime.now().date()
        import csv 
        count = 0
        with open("tasks.csv", "r", newline="") as file: 
                reader =csv.reader(file)
                for e in reader: 
                        count = count + 1

        due_date = datetime.strptime("due_date" , "%d/%m/%Y").date()
        days_remaining = (due_date - today).days
        if days_remaining < 0:
                print("You are overdue with your tasks")
        elif days_remaining <= 7:
                print("Please note that your task is close to the due date")
                
        valid_date = False
        while not valid_date:
                if due_date == False:
                        from datetime import datetime 
                try: 
                        if len(due_date) != 10:
                                raise ValueError("Incorrect format length")
                        date_obj = datetime.strptime(due_date, "%d/%m/%Y")
                        print("Valid date: ", date_obj)
                except ValueError as e: 
                                print("Error: ", e)
                if due_date == False:
                        valid_date = True
                        print("You have entered a valid date")
                if due_date > today:
                        valid_date = False
                        print("You are overdue with your tasks")
                else:
                        valid_date = True
                        print("Please note that your task is close to the due date")   


notifications()