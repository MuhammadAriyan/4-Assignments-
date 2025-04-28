def main():
    # Get user input
    user_input = input("Please enter a number: ")

    # Convert the input to an integer
    number = int(user_input)

    # Double the number
    doubled_number = number * 2

    while True:
        doubled_number *= 2
        print(f"The double of {number} is {doubled_number}.")
        
        if doubled_number > 100:
            print("The doubled number is greater than 100.")
            break
        
if __name__ == "__main__":
    main()