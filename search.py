import csv
def search_engine():
    #search_by = input("Enter name of task:")
    print("Search options below: ")
    print("----------------------")
    print("A: Search by task name")
    print("B: Search by task ID")
    print("C: Search by task due date")
    print("D: Search by category")
    search_by = input("How would you like to search? ")

    if search_by == "A":
        search_value = input("Search by task name: ")
        column = 1
    elif search_by == "B":
          search_value = input("Search by task ID:")
          column = 0

    with open("tasks.csv", "r", newline="") as file: 
                    reader =csv.reader(file)

                    for row in reader:
                        if row[column] == search_value:
                            print(row)
                            
                        else:
                            print("Checking...")
search_engine()