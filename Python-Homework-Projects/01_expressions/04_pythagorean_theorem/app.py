def main():
    ab: float = float(input("Enter the length of AB: "))
    ac: float = float(input("Enter the length of AC: "))
    # Calculate the length of BC using the Pythagorean theorem
    bc: float = (ab ** 2 + ac ** 2) ** 0.5 # square root of the sum of squares of AB and AC
    print(f"The length of BC is: {bc:.2f} units") # round to 2 decimal places