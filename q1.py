#Q1 Labfinalpractice
b = int(input("Enter the initial balance: "))
while True:
    t,a = input('Transaction type and amount ("done 0" to exit): ').split()
    if t == "done" and a == "0":
        print("> Current balance = %d THB."%b)
        break
    if t.isalpha() and a.isnumeric(): #to check if type is alpha and amount is > 0 since is numeric has to be only number (can't be float or negative number)
        a = int(a)
        if t == "D":
            b += a
            print("> Deposit = %d THB, current balance = %d THB."%(a,b))
        elif t == "W" and b > a:
            b -= a
            print("> Withdrawal = %d THB, current balance = %d THB."%(a,b))
        else:
            print("> Invalid transaction!")
    else:
            print("> Invalid transaction!")
    





#Thun's solution
b=int(input("Enter the initial balance: "))
while True:
    x,y=input('Transaction type and amount ("done 0" to exit): ').split()
    y=int(y)
    if x=="done" and y==0:
        print("> Current balance = %d THB."%b)
        break
    if x == "D" and y>=0:
        b+=y
        print("> Deposit =",y,"THB, current balance =",b,"THB.")
    elif x == "W" and y>=0 and b-y>=0:
        b-=y
        print("> Withdrawal =",y,"THB, current balance =",b,"THB.")
    else:
        print("> Invalid transaction!")
