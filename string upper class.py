#create class
class IOString():
    
            #constructor to set default value
        def __init__(self):
            self.strl = ""
        
            #function to get input from user
        def get_string(self):
            self.strl = input("Enter String:  ")
            
            #function to print the string in upper case
        def print_string(self):
                print("Result is: ", self.strl.upper())
                
#Object creation
str1 = IOString()
                
#call functions 
str1.get_string()
str1.print_string()