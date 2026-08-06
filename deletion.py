
def task_deletion():
 #task_id = input("Enter task ID to delete: ")
    import csv
    with open("tasks.csv" , "r", newline="") as file:
        reader = csv.reader(file)
    #    all_tasks = list(reader)
   
        updated_tasks = []
        task_id = input("Enter task ID to delete: ")
        reader = csv.reader(file)
        for row in reader:

            if row[0] != task_id: 
                with open("tasks5.csv", "a", newline="") as file:
                                    writer = csv.writer(file)
                                    writer.writerow(row)
      
            else: 
                    break
      

task_deletion()

    

