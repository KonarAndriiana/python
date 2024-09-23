def pridaj_produkt(zoznam, nazov, mnozstvo, cena):
    produkt = [nazov, mnozstvo, cena]
    zoznam.append(produkt)
    print(f"Produkt {nazov} bol pridany.")

def odstran_produkt(zoznam, nazov):
    for produkt in zoznam:
        if produkt[0] == nazov:
            zoznam.remove(produkt)
            print(f"Produkt {nazov} bol odstraneny zo zoznamu.")
            return
    print(f"Produkt s nazvom {nazov} sa nenasiel.")

def aktualizuj_produkt(zoznam, nazov, mnozstvo):
    for produkt in zoznam:
        if produkt[0] == nazov:
            produkt[1] = mnozstvo
            print(f"Produktu s nazvom {nazov} bolo aktualizovane mnozstvo na {mnozstvo}.")
            return
    print(f"Produkt s nazvom {nazov} sa nenasiel.")

def celkova_hodnota(zoznam):
    total = sum(produkt[1] * produkt[2] for produkt in zoznam)
    return total

def najdi_produkt(zoznam, nazov):
    for produkt in zoznam:
        if produkt[0] == nazov:
            return produkt
    return None

def produkty_s_nizkym_mnozstvom(zoznam, hranica):
    return [produkt for produkt in zoznam if produkt[1] < hranica]

zoznamProduktov = [
    ["Modra mrkva", 10, 0.3],
    ["Zemiaky", 10, 5.0],
    ["Brokolica", 3, 0.5],
    ["Hrach", 5, 1.0],
    ["Kalerab", 7, 0.8],
    ["Zeleva kapusta", 2, 1.5],
    ["Cervena repa", 4, 0.6]
]

pridaj_produkt(zoznamProduktov, "Kukurica", 5, 0.5)
print(zoznamProduktov)

odstran_produkt(zoznamProduktov, "Brokolica")
print(zoznamProduktov)

aktualizuj_produkt(zoznamProduktov, "Kukurica", 10)
print(zoznamProduktov)

print(f"Celkova hodnota produktov: {celkova_hodnota(zoznamProduktov)}")


print(najdi_produkt(zoznamProduktov, "Zemiaky"))

print(produkty_s_nizkym_mnozstvom(zoznamProduktov, 7))