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



# Creating child class of Vehicle 
class Car1(Vehicle):
    def top_speed(self):
        print(' Top speed is 130mph')


# Creating child class of Vehicle 
class Car2(Vehicle):
    def top_speed(self):
        print(' Top speed is 155mph')


# Calling methods from Car1 class
audi = Car1('Audi', 'TT', 'Silver')
audi.info()                 
audi.top_speed()

# Calling methods from Car2 class
bmw = Car2('BMW', 'Z4', 'Red')
bmw.info()                          
bmw.top_speed()
