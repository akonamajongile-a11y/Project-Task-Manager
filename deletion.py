# option = input("please select the option you want remove")

# if option == 0:
#     task_id = input(please enter task id)

import csv
with open("tasks.csv", "r", newline="") as file:
    data = csv.reader(file)

    all = []
    for everyline in data:
        all.append(everyline)
    for index,ev in enumerate(all):
       # [phiwe,cpt]
        if ev[0] == "phiwe7":
            all.pop(index)
            print("found her")
            break
        else:
            print("not found")
            with open("tasks2.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(ev)
            print(all)





    


    # all = []
    # for e in writer:
    #     if e[0] == '1': 
    #         print("e")

          