class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    
    def increment_odometer(self, value=100):
        self.odometer += value
    
    def to_string(self):
        print(f"A {self.year} {self.make.upper()} {self.model.upper()}. The car has completed {self.odometer}km.")
       
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.type = 'electric'
    
bmw = Car('SUV', 'bmw', 2006)
bmw.to_string()
bmw.increment_odometer()
print("We drove the car for 100km")
bmw.to_string()

bmw_electric = ElectricCar('SUV', 'bmw', 2021)
bmw_electric.to_string()
bmw_electric.increment_odometer()
print("We drove the car for 100km")
bmw_electric.to_string()
