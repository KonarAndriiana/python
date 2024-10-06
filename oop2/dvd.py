from medium import Medium 

class DVD(Medium):
    def __init__(self, title, author, year, duration, director):
        super().__init__(title, author, year)
        self.duration = duration
        self.director = director

    def __str__(self):
        return f'DVD: {self.title} ({self.year}), Režisér: {self.director}, Dĺžka: {self.duration} min., Dostupnosť: {self.available}'
