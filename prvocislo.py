num = int(input("Zadaj cele cislo:  "))
isPrime = True

if num <= 1:
    isPrime = False
else:
    for i in range(2, int(num ** 0.5) +1):
        if num % i == 0 :
            isPrime = False
            break

if isPrime :
    print(num, "je prvocislo")
else:
    print(num, "nie je prvocislo")
