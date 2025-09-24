class Dubai():
    def capital(self):
        print("Abu Dhabi is the capital of the UAE")
        
    def language(self):
        print("Arabic is the most widely spoken language in Dubai.")
        
    def type(self):
        print("India is a developing country.")
        
#Class 2
class USA():
    def capital(self):
        print("Washington, D.C is the capital of USA")
        
    def language(self):
        print("English is the primary language of USA")
        
    def type(self):
        print("USA is a developed country.")
        
#Object Creation
obj_dxb = Dubai()
obj_usa = USA()

#Common Interface
for country in (obj_dxb, obj_usa):
    country.capital()
    country.language()
    country.type()