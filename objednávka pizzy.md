# Návštevník si nejdříve zvolí velikost pizzy (S, M, L).
# Za velikost S se platí 100 Kč. za M 150 Kč a za L 200 Kč
# Poté se zeptáte, zda chce feferovnky. POkud ano, tak u velikosti S se bude platit navíc 20 Kč a u velikosti M a L 30 Kč navic
# Poté se ještě zeptáte, zda chce navštevnik syr navic. Pokud ano, tak si priplati dalších 15 Kč



print("Vítejte v aplikaci na objednání pizzy")

size = input("Jakou velikost pizzy chcete? S, M nebo L. ")
chilli_peppers = input("Chcete feferonky? A nebo N. ")
extra_cheese = input("Chcete extra syr? A nebo N. ")

bill = 0

if size == "S":
    bill += 100
elif size == "M":
    bill += 150
elif size == "L":
    bill += 200

if chilli_peppers == "A":
    if size != "S":
        bill += 30
    else:
        bill +=20

if extra_cheese == "A":
    bill += 15


print(f"Částka k zaplacení: {bill} Kč")
