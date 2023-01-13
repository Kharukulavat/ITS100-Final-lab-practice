#Q11 Labfinalpractice
print("Welcome to coin deposit machine")
deposit = {"1":0, "2":0, "5":0, "10":0}
balance = 0
while True:
    coin = input("Please insert coin: ")
    if coin == "done":
        break
    if coin == "1" or coin == "2" or coin == "5" or coin == "10":
        deposit[coin] += 1
        coin = int(coin)
        balance += coin
        print("You inserted %d baht coin"%coin)
        print("Current balance: %d baht"%balance)
        
    else:
        print("Only 1,2,5 and 10 baht coin are allowed")
print("<-----Deposit Summary----->")
for k,v in deposit.items():
    print("%s baht coins -> %d"%(k,v))
print("Deposit Amount: %d baht"%balance)