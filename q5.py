#Q5 Labfinalpractice

# lnwNattawin's solution
# for i in range(inp):
#     blank_space = inp - 1 - i
#     print(blank_space * " ",end="")
#     for _ in range(i+1):
#         print(inp,end = " ")
#     print()
    

#Thun's solution
while True:
    num = int(input("Enter an integer number(0 to exit): "))
    if 9 >= num > 0:
        x=num-1
        y=1
        for i in range(num):
            print(" "*x,end="")
            print("%d "%num*y,end="")
            print(" "*x,end="")
            print()
            x-=1
            y+=1
               
    else:
        print("Valid value is between 0 and 9!")


    
        