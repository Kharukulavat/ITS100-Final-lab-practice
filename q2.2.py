#Q2.2 Labfinalpractice
programs = {"ce":0, "che":0, "ec":0, "ie":0, "me":0}
name_gpa = {}
name_pg = {}
while True:
    inp = input("Input: ")
    if inp == "done":
        break
    name, pg, gpa = inp.split()
    if pg in programs.keys() and 4.00 >= float(gpa) >= 0.00:
        programs[pg] += 1
        if name not in name_gpa and name not in name_pg:
            name_gpa[name] = float(gpa)
            name_pg[name] = pg
    else:
        print("ERROR")
print("----SUMMARY----")
for k,v in programs.items(): #To print program summary
    print(k,"=",v)
print("----LIST----")
if len(name_gpa.keys()) != 0:
    for gpa in sorted(name_gpa.values(), reverse = True): # gpa from highest to lowest
        for k,v in name_gpa.items(): #k is name, v is gpa
            if gpa == v: #to let it print in order from highest gpa to lowest gpa
                print(k,name_pg[k],gpa) #k is name, name_pg[k] is program of that name, gpa is the sorted gpa
else:
    print("The list is empty.")