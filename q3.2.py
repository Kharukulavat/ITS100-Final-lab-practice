#Q3.2 Labfinalpractice
freq = {}
while True:
        vote = input("Input: ")
        if vote == "done":
            break
        if vote.isnumeric():
            vote = int(vote)
            if 1000 >= vote >= 1:
                if vote not in freq:
                    freq[vote] = 1
                else:
                    freq[vote] += 1
            else:
                print("ERROR")
        else:
            print("ERROR")
print("----Summary----")
if len(freq.keys()) != 0:
    for k,v in sorted(freq.items()):
        print(k,v)
else:
    print("This list is empty")