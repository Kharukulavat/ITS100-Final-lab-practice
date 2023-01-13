#Q7 Labfinalpractice
xo = []
while True:
    p = input("Input: ")
    if p == "o" or p == "x":
        xo.append(p)
    else:
        print("Wrong input")
        break
    if len(xo) == 9:
        print("-------")
        print("|%s|%s|%s|"%(xo[0],xo[1],xo[2]))
        print("-------")
        print("|%s|%s|%s|"%(xo[3],xo[4],xo[5]))
        print("-------")
        print("|%s|%s|%s|"%(xo[6],xo[7],xo[8]))
        print("-------")
        break