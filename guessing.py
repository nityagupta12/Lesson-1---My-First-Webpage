import random
def game():
    computer = random.randint(1, 10)
    guess = None
    attempts = 0
    
    print("Welcome to the Number Guessing Game! ")
    print("I'm thinking of a number between 1 and 10 ")
    
    while guess != computer:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < computer:
                print("Too low. Try again. ")
            elif guess > computer:
                print("Too high. Try again. ")
            else:
                print(f"Congratulations! You guessed a number in {attempts} attempts. ")
        except ValueError:
            print("Please enter a valid integer. ")
            
if __name__ == "__main__":
    game()