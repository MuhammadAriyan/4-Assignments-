MAX_TERM_VALUE : int = 10000

def main():
    currentNum = 0  
    nextNum = 1  # The 1st Fibonacci Number
    while currentNum <= MAX_TERM_VALUE:
        print(currentNum)
        numberAfterNext = currentNum + nextNum
        currentNum = nextNum
        nextNum = numberAfterNext


if __name__ == '__main__':
    main()