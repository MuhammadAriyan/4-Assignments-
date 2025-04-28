def main():
    dividend: float = float(input("Please enter an integer to be divided: "))
    divisor: float = float(input("Please enter an integer to divide by: "))
    
     
    quotient: int = dividend // divisor
    remainder: int = dividend % divisor 
    
    print(f"The quotient of {dividend} divided by {divisor} is {quotient}.")
    print(f"The remainder of {dividend} divided by {divisor} is {remainder}.")
    
    
if __name__ == "__main__":
    main()