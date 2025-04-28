def main():
    # Constants
    SPEED_OF_LIGHT:int = 299792458  # in meters per second
    
    MASS:float = float(input("Enter mass in kg: "))

    # Calculate energy using E=mc^2
    energy:float = MASS * (SPEED_OF_LIGHT ** 2)

    # Print the result
    print(f"Speed of light (C) = { SPEED_OF_LIGHT } m/s")
    print(f"mass (m) = {MASS} kg")
    print(f"Energy (E) = {energy} joules")
    print(f"The energy equivalent of {MASS} kg of mass is {energy} joules.")
    
if __name__ == "__main__":
    main()