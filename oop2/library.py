class Library:
    def __init__(self):
        self.media = []
        self.borrowed_count = 0  # Počet aktuálne vypožičaných médií

    def add_medium(self, medium):
        self.media.append(medium)
        print(f'Médium "{medium.title}" bolo pridané do knižnice.')

    def search_by_title(self, title):
        for medium in self.media:
            if medium.title.lower() == title.lower():
                return medium
        return None

    def list_available(self):
        print("Dostupné médiá v knižnici:")
        available_media = [medium for medium in self.media if medium.available]
        if not available_media:
            print("Žiadne médiá nie sú dostupné.")
        for medium in available_media:
            print(medium)

    def borrow_item(self, title):
        if self.borrowed_count >= 5:
            print("Nemôžete si vypožičať viac ako 5 médií naraz.")
            return

        medium = self.search_by_title(title)
        if medium:
            if medium.available:
                medium.borrow()
                self.borrowed_count += 1  # Zvýš počet vypožičaných médií
            else:
                print(f'Médium "{title}" už bolo vypožičané.')
        else:
            print(f'Médium s názvom "{title}" nebolo nájdené.')

    def return_item(self, title):
        medium = self.search_by_title(title)
        if medium:
            if not medium.available:
                medium.return_item()
                self.borrowed_count -= 1  # Zníž počet vypožičaných médií
            else:
                print(f'Médium "{title}" nebolo vypožičané.')
        else:
            print(f'Médium s názvom "{title}" nebolo nájdené.')

    def count_available(self):
        available_count = sum(1 for medium in self.media if medium.available)
        print(f'Počet dostupných médií: {available_count}')

    def filter_by_year(self, year):
        filtered_media = [medium for medium in self.media if medium.year == year]
        if filtered_media:
            print(f'Médiá vydané v roku {year}:')
            for medium in filtered_media:
                print(medium)
        else:
            print(f'Žiadne médiá z roku {year} neboli nájdené.')
