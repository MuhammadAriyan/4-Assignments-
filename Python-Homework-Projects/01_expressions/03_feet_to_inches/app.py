def main():
    feet: float = float(input("Enter number of feet: ")) 
    inches: float = feet * 12 # coversion from feet to inches; 12 inches is a foot
    print("That is", inches, "inches!")
    
    
if __name__ == '__main__':
    main()