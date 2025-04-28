def main ():
    list = []
    elem = input("Enter a something to add or enter to stop: ")
    while elem != "":
        list.append(elem)
        elem = input("Enter a something to add or enter to stop: ")
    print(list)
    
if __name__ == "__main__":
    main()