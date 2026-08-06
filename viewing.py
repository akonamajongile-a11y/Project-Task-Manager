
def view_task():
    import csv
    from colorama import Fore, Style
    with open("tasks.csv" , "r" , newline="") as file:
        reader = csv.reader(file)
        task_categories = "Task ID:       " + "Task Name:      " + "Category:      " + "Description:     " + "Priority:     " + "Due Date:      " + "Status:      "
        print(task_categories)
        print("-" * len(task_categories))   # Seperator line

        for everything in reader:
            print(everything[0]   + everything[1]   + everything[2]   + everything[3]   + everything[4]   + everything[5]) 
    print("Keep going, you're doing great!")

    priority = everything[4]
    if priority.lower() == "Medium":
                priority_text = f"{Fore.RED}{priority}{Style.RESET_ALL}"
    else:
                priority_text = f"{priority}"
       
       
view_task()