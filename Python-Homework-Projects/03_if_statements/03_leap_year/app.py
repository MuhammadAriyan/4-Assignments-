def main():
    leap_year = int(input("Enter a year: "))
    
    if (leap_year % 4 == 0 and leap_year % 100 != 0) or (leap_year % 400 == 0):
        print(f"{leap_year} is a leap year.")
    else:
        print(f"{leap_year} is not a leap year.")
        
if __name__ == "__main__":
    main()