def pridaj_vozidlo(vozovy_park, idx_vozidla, typ_vozidla, stav_vozidla, spotreba_vozidla, kilometre_vozidla, opravy_vozidla):
    vozovy_park[idx_vozidla] = {
        "typ": typ_vozidla, 
        "stav": stav_vozidla,
        "spotreba": spotreba_vozidla,
        "kilometre": kilometre_vozidla,
        "opravy": []
        }
    print(f"Vozidlo {idx_vozidla} pridane do vozoveho parku.")
    return vozovy_park

def pridaj_opravu(vozovy_park, idx_vozidla, oprava): 
    if idx_vozidla in vozovy_park:
        vozovy_park[idx_vozidla]["opravy"].append(oprava)
        print(f"Oprava {oprava} pridana k vozidlu {idx_vozidla}.")
    else:
        print(f"Vozidlo {idx_vozidla} nie je v vozovom parku.")
    return vozovy_park

def aktualizuj_stav(vozovy_park, idx_vozidla, novy_stav):
    if idx_vozidla in vozovy_park:
        vozovy_park[idx_vozidla]["stav"] = novy_stav
        print(f"Stav vozidla {idx_vozidla} aktualizovany.")
    else:
        print(f"Vozidlo {idx_vozidla} nie je v vozovom parku.")
    return vozovy_park

def aktualizuj_kilometre(vozovy_park, idx_vozidla, nove_kilometre):
    if idx_vozidla in vozovy_park:
        vozovy_park[idx_vozidla]["kilometre"] = nove_kilometre
        print(f"Kilometre vozidla {idx_vozidla} aktualizovane.")
    else:
        print(f"Vozidlo {idx_vozidla} nie je v vozovom parku.")
    return vozovy_park

def celkove_kilometre (vozovy_park):
    total = sum(vozovy_park[vozidlo]["kilometre"] for vozidlo in vozovy_park.values())
    return total

def zoznam_nefunkcnych(vozovy_park):
    nefunkcne_vozidla = []
    for vozidlo in vozovy_park:
        if vozovy_park[vozidlo]["stav"] == "nefunkcne":
            nefunkcne_vozidla.append(vozidlo)
    return nefunkcne_vozidla

def priemerna_spotreba(vozovy_park):
    celkova_spotreba = 0
    pocet_vozidiel = 0
    for vozidlo in vozovy_park:
        celkova_spotreba += vozovy_park[vozidlo]["spotreba"]
        pocet_vozidiel += 1
    return celkova_spotreba / pocet_vozidiel


vozovy_park = {}
vozovy_park = pridaj_vozidlo(vozovy_park, "001", "osobne", "nove", 5.5, 50, [])
vozovy_park = pridaj_vozidlo(vozovy_park, "002", "nakladne", "pouzivane", 10.5, 100, [])
vozovy_park = pridaj_vozidlo(vozovy_park, "003", "osobne", "pouzivane", 7.5, 200, [])
vozovy_park = pridaj_vozidlo(vozovy_park, "004", "nakladne", "nove", 15.5, 150, [])

vozovy_park = pridaj_opravu(vozovy_park, "002", "vymena pneumatik")
vozovy_park = pridaj_opravu(vozovy_park, "003", "vymena oleja")

vozovy_park = aktualizuj_stav(vozovy_park, "002", "nefunkcne")
vozovy_park = aktualizuj_stav(vozovy_park, "003", "funkcne")

print(vozovy_park)