from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, brand, model, year, mileage, service_interval, load_capacity):
        super().__init__(brand, model, year, mileage, service_interval)
        self.load_capacity = load_capacity

    def add_mileage(self, km):
        super().add_mileage(km)
        if self.mileage > self.service_interval + 10000:
            self.needs_service = True
    
    def __str__(self):
        return f'Nákladné auto: {self.brand} {self.model} {self.year} nosnosť: {self.load_capacity} a najazdené kilometre: {self.mileage}, potreba servisu: {self.needs_service}'