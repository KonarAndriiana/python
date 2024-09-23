num = int(input("Zadaj celé kladné číslo"))
nasiel = False
for i in range(1,11):
    for j in range(1,11):
        if num == i*j:
            nasiel = True
            print(f"Číslo {num} sa dá vyrátať pomocou čísel {i} * {j}")
            break
if not nasiel:
    print(f"Neexistujú také dve čísla od 1 po 10, ktorých súčin by bol {num}")