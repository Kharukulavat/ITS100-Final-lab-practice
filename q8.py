#Q8 Labfinalpractice
exchange = {}
while True:
    inp = input("Input: ")
    if inp == "end":
        break
    c,a = inp.split()
    if c in ["JPY","USD","EUR"]:
        try: 
            a = float(a)
            if float(a) >= 1:
                if c == "JPY":
                    jpy_baht = a*0.29
                    exchange["%.2f JPY"%a ] = "%.2f"%jpy_baht 
                    #To add the pair of (key:value) as (currency amount : THB of that amount)
                elif c == "USD":
                    usd_baht = a*31.99
                    exchange["%.2f USD"%a] = "%.2f"%usd_baht
                elif c == "EUR":
                    eur_baht = a*35.62
                    exchange["%.2f EUR"%a] = "%.2f"%eur_baht
            else:
                print("ERROR")
        except:
            print("ERROR")
    else:
        print("ERROR")
for k,v in exchange.items():
    print(k,"is",v,"THB")

