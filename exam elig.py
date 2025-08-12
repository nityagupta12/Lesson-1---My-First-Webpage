#Write a program to check whether the student can take an exam or not.
#Students will be allowed only in two conditions:
#If they have a medical cause (‘Y’ for yes and ‘N’ for no).
#If yes, then they will be allowed.
#If No, then check attendance
#If attendance is above 75, then allowed;
#otherwise, not allowed.





medical_cause = input ("Please enter do you have medical cause Yes or No")
attendance = int(input("Please enter your attendance"))

if medical_cause == 'Yes':
    print("Yes you are allowed")
else:
    if attendance > 75:
        print("You are allowed")
    else:
        print("No you are not allowed")