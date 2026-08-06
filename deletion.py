import os
import csv

def task_deletion():
    with open("tasks.csv" , "r", newline="") as file:
        reader = csv.reader(file)
   
        task_id = input("Enter task ID to delete: ")
        reader = csv.reader(file)
        for row in reader:

            if row[0] != task_id: 
                with open("tasks5.csv", "a", newline="") as file:
                                    writer = csv.writer(file)
                                    writer.writerow(row)
      
            else: 
               with open("tasks5.csv", "a", newline="") as file:
                    writer = csv.writer(file)
                    
    os.rename("tasks.csv", "tasksold.csv")           
    os.rename("tasks5.csv", "tasks.csv")         
    os.remove("tasksold.csv")  

task_deletion()

    

   

          