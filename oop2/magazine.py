from medium import Medium

class Magazine(Medium):
    def __init__(self, title, author, year, issue):
        super().__init__(title, author, year)
        self.issue = issue

    def __str__(self):
        return f'Časopis: {self.title}, Autor: {self.author}, Vydanie: {self.issue}, Rok: {self.year}, Dostupnosť: {self.available}'
