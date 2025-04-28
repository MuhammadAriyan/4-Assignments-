import random

MAX_DICE = 6

def roll_dice():
    dic1= random.randint(1, MAX_DICE)
    dic2= random.randint(1, MAX_DICE)
    total = dic1 + dic2
    print(f"Dice 1: {dic1}, Dice 2: {dic2}, Total: {total}")
    return total
    
def main():
    total = 0
    for _ in range(3):
        print(f'Rolling the dice...')
        total += roll_dice()
        
    print(f'Total after 3 rolls: {total}')

if __name__ == '__main__':
    main()