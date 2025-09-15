#create class
class Parrot:
    
    #class attribute
    species = "bird"
    
    #instance attribute
    def __init__(self, name, age):
            self.name = name
            self.age = age
        
    #instantiate the Parrot class
Nitya = Parrot("Nitya", 13)
Deetya = Parrot("Deetya", 16)
    
    #access the class attributes
print("Nitya is a {}" .format(Nitya.species))
print("Deetya is also a {}" .format(Deetya.species))
    
    #access the instance attributes 
print("{} is {} years old" .format( Nitya.name, Nitya.age))
print("{} is {} years old" .format(Deetya.name, Deetya.age))
    
        