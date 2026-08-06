# option = input("please select the option you want remove")

# if option == 0:
#     task_id = input(please enter task id)
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
                updated_tasks.append(row)
      
            else: 
                with open("tasks5.csv", "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(updated_tasks)
                    break
      
    

task_deletion()

    


    # all = []
    # for e in writer:
    #     if e[0] == '1': 
    #         print("e")

          