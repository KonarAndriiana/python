from library import Library
from book import Book 
from magazine import Magazine
from dvd import DVD


def main():
    library = Library()

    while True:
        print("\n1. Pridaj nové médium")
        print("2. Vyhľadaj médium podľa názvu")
        print("3. Zobraz všetky dostupné médiá")
        print("4. Vypožičaj médium")
        print("5. Vráť médium")
        print("6. Zobraz počet dostupných médií")
        print("7. Filtrovať médiá podľa roku vydania")
        print("8. Ukončiť")
        
        choice = input("Vyber možnosť: ")

        if choice == "1":
            media_type = input("Typ média (book, magazine, dvd): ").lower()
            title = input("Názov: ")
            author = input("Autor: ")
            year = int(input("Rok vydania: "))

            if media_type == "book":
                genre = input("Žáner: ")
                book = Book(title, author, year, genre)
                library.add_medium(book)
            elif media_type == "magazine":
                issue = int(input("Číslo vydania: "))
                magazine = Magazine(title, author, year, issue)
                library.add_medium(magazine)
            elif media_type == "dvd":
                duration = int(input("Dĺžka (min): "))
                director = input("Režisér: ")
                dvd = DVD(title, author, year, duration, director)
                library.add_medium(dvd)
            else:
                print("Neplatný typ média.")

        elif choice == "2":
            title = input("Zadaj názov média: ")
            medium = library.search_by_title(title)
            if medium:
                print(medium)
            else:
                print(f'Médium "{title}" nebolo nájdené.')

        elif choice == "3":
            library.list_available()

        elif choice == "4":
            title = input("Zadaj názov média na vypožičanie: ")
            library.borrow_item(title)

        elif choice == "5":
            title = input("Zadaj názov média na vrátenie: ")
            library.return_item(title)

        elif choice == "6":
            library.count_available()

        elif choice == "7":
            year = int(input("Zadaj rok vydania: "))
            library.filter_by_year(year)

        elif choice == "8":
            print("Ukončujem program.")
            break

        else:
            print("Neplatná možnosť.")

if __name__ == "__main__":
    main()

