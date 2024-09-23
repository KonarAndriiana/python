import random

rand_num= random.randint(1 , 100)
pokusy = 0 
guess = 0

print("Hra hadaj cislo od 1 do 100")

while guess != rand_num:
    guess = int(input("Zadaj cislo: "))
    pokusy += 1

    if guess > rand_num:
        print("hadane cislo je menej")
    elif guess < rand_num:
        print("hadane cislo je viac")
    elif guess == rand_num:
        print("hadane cislo je spravne" , pokusy , "pokusov")
        break
    else:
        print("Zadal si zle cislo")