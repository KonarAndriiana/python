class Vehicle():

    def __init__(self, brand, model, year, mileage, service_interval):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.service_interval = service_interval
        self.needs_service = False

    def add_mileage(self, km):
        self.mileage += km
        if self.mileage >= self.service_interval:
            self.needs_service = True

    def perform_service(self):
        self.needs_service = False
        print(f"Bol vykonaný servis na vozidle {self.brand} {self.model}")

    def __str__(self):
        return f'{self.brand}, {self.model}, {self.year}, Najazdené kilometre: {self.mileage}  Potreba servisu: {self.needs_service}'