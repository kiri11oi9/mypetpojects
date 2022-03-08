class Car:
    def __init__(self, gas, capacity, gas_per_km, km = 0):
        self.g = gas
        self.c = capacity
        self.gkm = gas_per_km
        self.k = km

    def fill(self, litre):
        to_full = self.c - self.g
        if litre > to_full:
            self.g = self.c
            print(f"Не вместилось литров: {litre-to_full}")
        else:
            self.g += litre
            print(f"В машине {self.g} литров")


    def ride(self, distance):
        max_dist = int(self.g / self.gkm)
        if distance > max_dist:
            print("Проехали ", int(max_dist)," километров, кончился бензин")
            self.k += int(max_dist)
            self.g = 0
        else:
            print("Проехали ", distance," км")
            self.k += distance
            self.g -= distance * self.gkm
        #return self.k


car1 = Car(15, 50, 1)
car1.ride(10)
print(car1.g)
car1.ride(10)
print(car1.g)
print(car1.k)
