def addnum(a:list[int] | int) -> int:
    total:int = 0
    for i in a:
        total += i
        
    return total
    
def main():
    print(addnum([1, 2, 3, 4, 5]))
    
if __name__ == "__main__":
    main()
    