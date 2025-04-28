MINIMUM_HEIGHT : int = 50

def main() -> None:
    
    while True:
        try:
            inp_height = float(input("Enter your height : "))
            if inp_height < 0:
                print("Height cannot be negative. Please enter a valid height.")
                continue
            if inp_height >= MINIMUM_HEIGHT:
                print("You are tall enough to ride the roller coaster.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
            
if __name__ == "__main__":
    main()