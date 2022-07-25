# Defining new object, parent class, and adding attributes
class Vehicle:

    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def info(self):
        print('Details:\n', self.make, self.model, self.color)

    def top_speed(self):
        print(' Top speed is unknown')



# Creating child class of Vehicle and adding attributes
class Car1(Vehicle):
    def layout(self):
        print(' FWD or AWD')
    def seats(self):
        print(' 2- or 4-seater')
    def top_speed(self):
        print(' Top speed is 130mph')
    


# Creating child class of Vehicle and adding attirbutes
class Car2(Vehicle):
    def production(self):
        print(' Produced in South Carolina')
    def age(self):
        print(' First-generation released in 2003')
    def top_speed(self):
        print(' Top speed is 155mph')


# Calling methods from Car1 class
audi = Car1('Audi', 'TT', 'Silver')
audi.info()
audi.layout()
audi.seats()
audi.top_speed()

# Calling methods from Car2 class
bmw = Car2('BMW', 'Z4', 'Red')
bmw.info()
bmw.production()
bmw.age()
bmw.top_speed()
