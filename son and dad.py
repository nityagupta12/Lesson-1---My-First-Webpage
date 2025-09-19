#Parent class
class dad:
    def __init__(self, eyes, aggressive):
        self.eyes = eyes
        self.aggressive = aggressive
        
    def display(self):
        print("Your eye color is", self.eyes)
        print("You are aggressive", self.aggressive)
        
#child class
class son(dad):
    
    def __init__(self,name,age, eyes, aggressive):
        self.name = name
        self.age = age
        
        #invoking the __init__ of parent class
        #to access it's attributes
        super().__init__(eyes, aggressive)
              
#Object Creation
obj = son("Penguin", 8, "blue", True)

#calling method display
obj.display()
