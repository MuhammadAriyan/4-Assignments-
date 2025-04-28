import random as rd 
MAX = 100
def main():
    for i in range(0, 12):
        random_number = rd.randint(1, MAX)
        print(random_number)
        
if __name__ == "__main__":
    main()