import csv
def search_engine():
    
    print("Search options below: ")
    print("----------------------")
    print("A: Search by task name")
    print("B: Search by task ID")
    print("C: Search by task due date")
    print("D: Search by category")
    #print("E: Search by status")
    search_by = input("How would you like to search? ")

    if search_by == "A":
        search_value = input("Search by task name: ")
        column = 1
    elif search_by == "B":
          search_value = input("Search by task ID:")
          column = 0
    elif search_by == "C":
          search_value = input("Search task by its due date: ")
          column = 3
    elif search_by == "D":
          search_value = input("Search task by category: ")
          column = 5
    else:
          print("You have entered invalid option")

    found = False
    with open("tasks.csv", "r", newline="") as file: 
                    reader =csv.reader(file)

                    for row in reader:
                        if row[column] == search_value:
                            print(row)
                            found = True
                             

    if not found:
          print("Nothing Found")        
                            
search_engine()



