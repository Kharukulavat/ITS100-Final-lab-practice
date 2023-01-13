#Q2 Labfinalpractice
ns = {}
def NameandScore():
    while True:
        inp = input("Enter student name and score: ") 
        if inp == "end" or inp == "end 0":
            break
        name,score = inp.split()
        if 100 >= int(score) >= 0:
            if name not in ns:
                ns[name] = int(score)
            else:
                print("Duplicated name!")
        else:
            print("Invalid score!")
            
def SortedScore():
    sorted_score = sorted(ns.values(), reverse =True) #To create list of sorted score from high to low
    for i in sorted_score:
        if sorted_score.count(i) != 1: #delete the duplicated value to avoid printing the duplicated condition in next for loop
            sorted_score.remove(i) #remove until it has 1 left so that the for loop below can avoid duplicated conditions when we have more than 1 same score Ex. having [80,60,60] 
    print("List:")
    if len(sorted_score) > 0:
        for i in sorted_score: #check for each score
            for k,v in ns.items():
                if i == v: #To print only the condition of that score equal to that value in the dictionary and also able to print key (For printing value while able to print key)
                    #Ex. having [80,60,60] will get us duplicated output in '60' condition
                    print("%-10s %s"%(k,v))
    else:
        print("> empty list!")
        
NameandScore()
SortedScore()







#P'Time's solution 
#Using itemgetter
from operator import itemgetter

def print_sorted(dict):
  for key,value in sorted(dict.items(),key=itemgetter(1),reverse=True):
    print("%s \t %d"%(key,value))

students={}
while True:
  name,score=input("Enter student name and score: ").split()
  if name=="end" and score=="0":
    break
  score=int(score)
  if score<0 or score>100:
    print("Invalid score!")
  elif name not in students:
    students[name]=score
  else:
    print("Duplicated name!")
print("List: ")
if len(students)==0:
  print("> empty list!")
else:
  print_sorted(students)
    


