from abc import ABC, abstractmethod

class Medium(ABC):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f'Médium "{self.title}" bolo úspešne vypožičané.')
        else:
            print(f'Médium "{self.title}" nie je dostupné.')

    def return_item(self):
        self.available = True
        print(f'Médium "{self.title}" bolo vrátené.')

    @abstractmethod
    def __str__(self):
        pass
