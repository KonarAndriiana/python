from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, year, mileage, service_interval, seats):
        super().__init__(brand, model, year, mileage, service_interval)
        self.seats = seats

    def __str__(self):
        return f'Osobné auto: {self.brand} {self.model} {self.year} s počtom sedadiel: {self.seats} a najazdené kilometre: {self.mileage}, potreba servisu: {self.needs_service}'
    