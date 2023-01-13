#Q3 Labfinalpractice
point = 100
while True:
    c,p = input("Command: ").split()
    if c == "done" and p == "0":
        break
    p = int(p)
    if p > 0:
        if c == "P":
            earn = p//50 #Floor division 
            point += earn
            print("You earned %d points"%earn)
            print("Your accumulated points = %d points"%point)
        elif c == "R":
            if point > p:
                point -= p
                print("You redeemed %d points"%p)
                print("Your accumulated points = %d points"%point)
            else:
                print("Not enough points")
        else:
            print("Invalid command")
    else:
        print("Invalid command")





#Thun's solution
# b=100
# while True:
#     x,y=input('Command: ').split()
#     y=int(y)
#     if x=="done" and y==0:
#         break
#     if x == "P" and y>=0:
#         b+=y//50
#         print("You earned",y//50,"points\nYour accumulated points =",b,"points")
#         continue
#     if x == "R" and y>=0 and b-y>=0:
#         b-=y
#         print("You redeemed",y,"points\nYour accumulated points =",b,"points")
#         continue
#     if x == "R" and y>=0 and b-y<0:
#         print("Not enough points")
#         continue
#     print("Invalid command")
