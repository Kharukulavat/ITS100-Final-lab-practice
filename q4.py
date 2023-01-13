#Q4 Labfinalpractice
ns = {}
totalscore = 0
while True:
  inp = input("Input: ")
  if inp == "done" and totalscore == 0:
    print("No players")
  if inp == "done":
    break
  
  name,score = inp.split()
  if name not in ns:
      if score.isnumeric():
        score = int(score)
        totalscore += score
        ns[name] = score
      else:
        print("Invalid input")
  else:
    print("Duplicated player")

if totalscore != 0:
  sorted_score = sorted(ns.values(),reverse =True)
  average = totalscore/len(sorted_score)
  for i in sorted_score:
    for k,v in ns.items():
      if i == v:
        if i == sorted_score[0]:
          print("%s\t%d\tGold"%(k,v))
        elif i > average:
          print("%s\t%d\tSilver"%(k,v))
        else:
          print("%s\t%d"%(k,v))
      
  


















