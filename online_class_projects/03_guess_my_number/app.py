import random as rd 

def main():
    random_number = rd.randint(1, 100)
    
    while True:
        try:
            user_input = int(input("Guess a number between 1 and 100: "))
            
            if user_input < 1 or user_input > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            if user_input < random_number:
                print("Too low! Try again.")
            elif user_input > random_number:
                print("Too high! Try again.")
            else:
                print("Congratulations! You've guessed the number.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
if __name__ == "__main__":
    main()