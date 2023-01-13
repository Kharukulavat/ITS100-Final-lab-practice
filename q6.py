#Q6 Labfinalpractice
pair = {}
totalscore = 0
while True:
    sid,score = input("Enter student ID and score: ").split()
    if sid == "done" and score == "0":
        break
    if sid.isnumeric() and len(sid) == 4:
        sid = int(sid)
        if score.isnumeric() and 100 >= int(score) >= 0:
            score = int(score)
            if sid not in pair:
                pair[sid] = score
                totalscore += score
            else:
                print("The ID is already recorded!")
        else:
            print("Invalid score!")
    else:
        print("Invalid ID format!")

def ListOfStudent():
    totalsd = len(pair.keys())
    print("List:")
    if totalsd == 0:
        print("> no score is recorded!")
    else:
        average = totalscore / totalsd
        for k,v in sorted(pair.items()):
            print("%d \t %d"%(k,v))
        print("There are %d student(s). The average score is %.2f points."%(totalsd,average))

ListOfStudent()
        
    