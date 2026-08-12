
def view_task():
    import csv
    with open("tasks.csv" , "r" , newline="") as file:
        reader = csv.reader(file)
        task_categories = (
            f"{'Task ID':<10}\t"
            f"{'Task Name':<20}\t"
            f"{'Category':<12}\t"
            f"{'Description':<35}\t"
            f"{'Priority':<10}\t"
            f"{'Due Date':<15}\t"
            f"{'Status':<10}\t")
        print("=" * len(task_categories))
        print(task_categories)
        print("=" * len(task_categories))   # Seperator line

        for everything in reader:
            print(
                f"{everything[0]:<10}"   #/t/t/t/
                f"{everything[1]:<20}"
                f"{everything[2]:<12}"
                f"{everything[3]:<35}"
                f"{everything[4]:<10}"
                f"{everything[5]:<15}"
                f"{everything[6]:<10}")
            
    print("-" * len(task_categories))       
    print(" " * 40 + "Keep going, you're doing great :)") 

<<<<<<< HEAD


    RED = "\033[31m"
    RESET = "\033[0m"
    everything[4] = "High", "Low", "Medium"
    if everything[4] == "High":
      print(f"{RED}everything[4]:<10{RESET}")
       # f"{Fore.RED} + {everything[4]:<10}"

         #{Style.RESET_ALL}"

<<<<<<< HEAD
=======
                f"{everything[0]:<10}\t"
                f"{everything[1]:<20}\t"
                f"{everything[2]:<12}\t"
                f"{everything[3]:<35}\t"
                f"{everything[4]:<10}\t"
                f"{everything[5]:<15}\t"
                f"{everything[6]:<10}\t")
            
    print("=" * len(task_categories))       
    print(" " * 50 + "You're doing amazing sweetie!") 
    print("=" * len(task_categories))
       
view_task()
>>>>>>> viewing
=======

view_task()
>>>>>>> dashboard.py
=======
>>>>>>> d1748ada722f68f9228d5f95314d8ab6d7280a41
