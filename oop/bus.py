from vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, brand, model, year, mileage, service_interval, passenger_capacity):
        super().__init__(brand, model, year, mileage, service_interval)
        self.passenger_capacity = passenger_capacity

    def __str__(self):
         return f'Autobus: {self.brand} {self.model} {self.year} kapacita pasažierov: {self.passenger_capacity} a najazdené kilometre: {self.mileage}, potreba servisu: {self.needs_service}'