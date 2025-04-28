import random as rd

compNumber = rd.randint(1, 10) # Random number between 1 and 10
print("Welcome to the Guess the Number game!")
print("I have selected a number between 1 and 10. Can you guess it?")


while True:
    try:
        number = int(input("Enter a number between 1 and 10: "))
        if number == compNumber:
            print("Congratulations! You've guessed the correct number.")
            break
        elif number < compNumber:
            print("Too low! Try again.")
        elif number > compNumber:
            print("Too high! Try again.")
        else:
            print("Please enter a valid number between 1 and 100.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
        
