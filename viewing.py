
def view_task():
    import csv
    from colorama import Fore, Style
    with open("tasks.csv" , "r" , newline="") as file:
        reader = csv.reader(file)
        task_categories = (
            f"{'Task ID':<10}"
            f"{'Task Name':<20}"
            f"{'Category':<12}"
            f"{'Description':<35}"
            f"{'Priority':<10}"
            f"{'Due Date':<15}"
            f"{'Status':<10}")
        print(task_categories)
        print("-" * len(task_categories))   # Seperator line

        for everything in reader:
            print(
                f"{everything[0]:<10}"
                f"{everything[1]:<20}"
                f"{everything[2]:<12}"
                f"{everything[3]:<35}"
                f"{everything[4]:<10}"
                f"{everything[5]:<15}"
                f"{everything[6]:<10}")
            
    print("-" * len(task_categories))       
    print(" " * 40 + "Keep going, you're doing great :)") 

    
    everything[4] = "High", "Low", "Medium"
    if everything[4] == "High":
        f"{Fore.RED}{everything[4]:<10}{Style.RESET_ALL}"

    
       
       
view_task()
