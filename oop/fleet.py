from car import Car
from bus import Bus
from truck import Truck

class Fleet():
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Vozidlo {vehicle.brand} {vehicle.model} bolo pridané do vozového parku")

    def show_fleet(self):
        if not self.vehicles:
            print("Vozový park je prázdny")
        else:
            for vehicle in self.vehicles:
                print(vehicle)

    def find_vehicle_by_brand(self, brand):
        found_vehicles = [vehicle for vehicle in self.vehicles if vehicle.brand == brand]
        if not found_vehicles:
            print(f"Žiadne vozidlá značky {brand} sa nenašli")
        else:
            for vehicle in found_vehicles:
                print(vehicle)