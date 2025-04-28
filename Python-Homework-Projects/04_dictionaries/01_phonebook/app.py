def writePhonebook():
    phonebook = {}                   # Create empty phonebook
    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook

def readPhonebook(phonebook):
    print("Phonebook:")
    for name, number in phonebook.items():
        print(f"{name}: {number}")
        
def lookupPhonebook(phonebook):
    while True:
        name = input("Enter name to lookup (or press Enter to exit): ")
        if name == "":
            break
        if name in phonebook:
            print(f"{name}: {phonebook[name]}")
        else:
            print(f"{name} not found in phonebook.")
            
def main():
    phonebook = writePhonebook()    # Write phonebook to file
    readPhonebook(phonebook)         # Read phonebook from file
    lookupPhonebook(phonebook)       # Lookup names in phonebook
    
if __name__ == "__main__":
    main()
