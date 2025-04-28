PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main() -> None:
    print("Peturksbouipo: ", PETURKSBOUIPO_AGE)
    print("Stanlau: ", STANLAU_AGE)
    print("Mayengua: ", MAYENGUA_AGE)

    user_input = int(input("Enter your age : "))
    
    if user_input >= PETURKSBOUIPO_AGE:
        print("You are eligible to vote in Peturksbouipo.")
    else:
        print("You are not eligible to vote in Peturksbouipo.")
        
    
    if user_input >= STANLAU_AGE:
        print("You are eligible to vote in stanlau.")
    else:
        print("You are not eligible to vote in stanlau.")
        
    if user_input >= MAYENGUA_AGE:
        print("You are eligible to vote in mayengua.")
    else:
        print("You are not eligible to vote in mayengua.")
    
    
    
if __name__ == "__main__":
    main()