


# Creating Protected Class
class Protected:
   def __init__(self): 
      self.__privateAttribute = 3   # Double-underscore to indicate private attribute, should not be altered
      self._privateAttribute = 5    # Single-underscore to indicate protected attribute
      
   def getAttribute(self):
      print(self.__privateAttribute)



# "obj" as Protected class, calling private + protected arguments 
obj = Protected()
obj.__privateAttribute = 10 
obj.getAttribute()



print(obj.__privateAttribute)
