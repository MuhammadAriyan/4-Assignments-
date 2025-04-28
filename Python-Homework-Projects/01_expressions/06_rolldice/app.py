import random as rd

def main():
    # Simulate rolling a die
    die_roll1 = rd.randint(1, 6)
    die_roll2 = rd.randint(1, 6)
    
    print(f"Die 1: {die_roll1}")
    print(f"Die 2: {die_roll2}")
    print(f"Sum of both dice: {die_roll1 + die_roll2}")
    
if __name__ == "__main__":  
    main()