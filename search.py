def search_engine():
    #print("Search by ")
    search_by = input("enter name of task")
    import csv
    with open("tasks.csv", "r", newline="") as file: 
                    reader =csv.reader(file)

                    for row in reader:
                        if row[1] == search_by:
                            print(row)
                            
                        else:
                            print("Checking...")
search_engine()