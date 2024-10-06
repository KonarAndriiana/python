from fleet import Fleet
from car import Car
from bus import Bus
from truck import Truck

fleet = Fleet()

car1 = Car("Toyota", "Yaris", 2021, 10000, 15000, 5)
car2 = Car("Lamborghini", "Urus", 2024, 100, 12000, 5)
bus1 = Bus("Mercedes", "Citaro", 2018, 200000, 100000, 48)

fleet.add_vehicle(car1)
fleet.add_vehicle(car2)
fleet.add_vehicle(bus1)

fleet.show_fleet()

