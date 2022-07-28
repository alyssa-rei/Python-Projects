# Defining new object, parent class, and adding attribute
class Person:

    def __init__(self, name):
        self.name = name

    def greeting(self):
        print('Hello,', self.name)



# Creating child class of Person and adding two, unique attributes
class Student(Person):
    # Calling __init__ of parent class, Person
    def __init__(self, name, major, grad):
        super().__init__(name)
        self.major = major
        self.grad = grad

    def print_major(self):
        print(' Major: {}'.format(self.major))

    def print_grad(self):
        print(' Expected Graduation: {}'.format(self.grad))


# Creating child class of Person and adding two, unique attributes
class Employee(Person):
    # Calling __init__ of parent class, Person
    def __init__(self, name, department, division):
        super().__init__(name)
        self.department = department
        self.division = division

    def print_dept(self):
        print(' Department: {}'.format(self.department))

    def print_divs(self):
        print(' Division: {}'.format(self.division))


# Calling methods from Student class
s1 = Student('Zach', 'Business', 2024)
s1.greeting()
s1.print_major()
s1.print_grad()


# Calling methods from Employee class
e1 = Employee('Thomas', 'Science', 'Chemistry')
e1.greeting()
e1.print_dept()
e1.print_divs()
