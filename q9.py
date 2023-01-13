#Q9 Labfinalpractice
l = {}
while True:
    inp = input("Input: ")
    if inp == "done":
        break
    name,amount = inp.split()
    if name.isalpha() and amount.isnumeric():
        amount = int(amount)
        if name not in l:
            l[name] = amount
        else:
            l[name] += amount
    else:
        print("Invalid input!")
if len(l.keys()) != 0:
    print("###Summary###")
    for k,v in l.items():
        print("Total Number of %s : %d"%(k,v))
else:
    print("Empty List")
    print("###Summary###")