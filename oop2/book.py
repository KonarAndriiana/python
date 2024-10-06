from medium import Medium

class Book(Medium):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre

    def __str__(self):
        return f'Kniha: {self.title} od {self.author} ({self.year}), Žáner: {self.genre}, Dostupnosť: {self.available}'
