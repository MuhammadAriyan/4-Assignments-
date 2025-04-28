fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
 
def main():
    total_cost = 0
    for fruit in fruits:
        print(f"{fruit}: {fruits[fruit]}")
        buy = input(f"how many ({fruit}) do you want to buy? : ")
        total_cost += fruits[fruit] * int(buy)
        
    print(f"Total cost: {total_cost}")
    
if __name__ == "__main__":
    main()
        