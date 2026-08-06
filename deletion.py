# option = input("please select the option you want remove")

# if option == 0:
#     task_id = input(please enter task id)

import csv
with open("tasks.csv", "r", newline="") as file:
    data = csv.reader(file)

    all = []
    for everyline in data:
        all.append(everyline)
    for ev in all:
       # [phiwe,cpt]
        if ev[0] == "phiwe7":
            all.pop(7)
        else:
            print("not found")
        print(all)

with open("tasks.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(all)




    


    # all = []
    # for e in writer:
    #     if e[0] == '1': 
    #         print("e")

          