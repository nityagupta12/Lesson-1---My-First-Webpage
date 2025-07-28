#Write a program to calculate the number of notes in the given amount?


#Taking total amount as input from user
Amount =int(input("Please Enter Amount for Withdraw :"))

#Calculating the number of notes of different denominations
note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10


print(" Notes of 100 dirhams", note_1)
print(" Notes of 50 dirhams", note_2)
print(" Notes of 25 dirhams", note_3)

