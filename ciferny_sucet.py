num = int(input("Zadaj kladne cele cislo:  "))
num_copy = num
sucet = 0

while num > 0:
    zvysok_po_deleni = num % 10
    sucet += zvysok_po_deleni
    num = num // 10 

    print(f"Ciferny sucet cila {num_copy} je {sucet}")