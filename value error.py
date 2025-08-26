#using a try and except
try:
    number = int(input("ENTER A NUMBER:  "))
    print("The number entered is", number)
    #usine value error
except ValueError as ex:
    print("Exception: ", ex)