def getNum()-> list[int] | int:
    lst = []
    while True:
        try:
            n = int(input("Enter a number: "))
            if n < 0:
                raise ValueError("Negative numbers are not allowed.")
            if n <= 0:
                lst.append(n)
                continue
            if n == '':
                break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a non-negative integer.")
            
    return lst if len(lst) > 0 else 0

def count_nums(lst: list[int]) -> int:
    num_dict = {}
    
    for num in lst:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    
    return num_dict

def main():
    lst = getNum()
    if lst == 0:
        print("No numbers were entered.")
        return
    
    num_dict = count_nums(lst)
    
    for num, count in num_dict.items():
        print(f"{num}: {count}")