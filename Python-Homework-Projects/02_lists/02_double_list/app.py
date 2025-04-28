def double_list(a:list[int]) -> list[int]:
    return [i * 2 for i in a]

def main():
    print(double_list([1, 2, 3, 4, 5]))
    
if __name__ == "__main__":
    main()