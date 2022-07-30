


# Importing abstract method
from abc import ABC, abstractmethod

# Creating abstract, parent class
class Cars(ABC):
    @abstractmethod 
    def style(self):
        pass
    def body_style(self):
        print("Coupes and hatchbacks have different body styles.")

class Coupe(Cars):
    def style(self): 
        print("Coupes have two doors.")

class Hatchback(Cars):
    def style(self):
        print("Hatchbacks have three or five doors.")



# Calling parent, child methods
C = Coupe()
C.body_style()
C.style()

H = Hatchback()
H.body_style()
H.style()

