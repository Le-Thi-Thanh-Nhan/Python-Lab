class Vehiche:
    def __init__(self, make = '', model = '', year = 0):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehiche):
    def __init__(self, make = '', model = '', year = 0, num_doors = 0):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def HienThi(self):
        print(f'Car: {self.make} {self.model} {self.year} {self.num_doors}')

car = Car('Toyota', 'Corolla', 2015, 4)
car.HienThi()

        