def search_engine():
    #print("Search by ")
    import csv
    with open("tasks.csv", "r", newline="") as file: 
                    reader =csv.reader(file)

                    for e in reader:
                        if e[1] == " sewing":
                            print(e)
                            break
                        else:
                            print("Checking...")
search_engine()