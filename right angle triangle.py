#take input
print("Half Pyramid Pattern of Stars (*):")
n = int(input("enter the number of rows: "))
#outer loop to handle number of coloumns
for i in range(n):
   #inner loop to handle number of coloumns
    for j in range(i+1):
     #display result
      print("* ", end="")
    print()