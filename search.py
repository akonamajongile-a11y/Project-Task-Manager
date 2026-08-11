import csv
def search_engine():

    print("----------------------")
    print("Search options below: ")
    print("----------------------")
    print("A: Search by task name")
    print("B: Search by task ID")
    print("C: Search by task due date")
    print("D: Search by category")
    
    searchokay = False
    while not searchokay:
        search_by = input("Enter the option from above: ").upper()
        search_value = ""
        column = 0
        if search_by == "A":
            search_value = input("Search by task name: ")
            print("------------------------------------")
            column = 1
            searchokay = True
        elif search_by == "B":
            search_value = input("Search by task ID:")
            print("---------------------------------")
            column = 0
            searchokay = True
        elif search_by == "C":
            search_value = input("Search task by its due date: ")
            print("--------------------------------------------")
            column = 3
            searchokay = True
        elif search_by == "D":
            search_value = input("Search task by category: ")
            print("----------------------------------------")
            column = 5
            searchokay = True
        else:
            searchokay = False
            

    found = False
    with open("tasks.csv", "r", newline="") as file: 
                    reader =csv.reader(file)

                    for row in reader:
                        if row[column] == search_value.lower():
                                print(row)
                                found = True            
     
    if not found:
          print("Nothing Found")  
          again = ""
          while again not in ["Y", "N"]:
                  again = input("Would you like to search again? (Y/N): ").upper()

                  if again not in ["Y", "N"]:
                        print("You have entered invalid option, select between Y & N only")
                    
          if again == "Y":
                search_engine()    
          else:
               print("Thanks bye!")

                            







