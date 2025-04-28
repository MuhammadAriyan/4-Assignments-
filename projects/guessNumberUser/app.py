import random as rd

def compGuess():
    low = 0
    high = 101
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = rd.randint(low, high)
        elif low == high:
            guess = low
        else:
            print("Your number is out of Range of 1 to 100.")
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("Please enter H, L, or C.")
        
    print(f"I guessed your number, {guess} correctly!")
    return True
compNumber = rd.randint(1, 100) # Random number between 1 and 10
print("Welcome to the Guess the Number game!")
print("select a number between 1 and 100. I will now start guessing it!")

input("Press Enter to continue...")
print("I will now start guessing your number!")
compGuess()