import time
def main():
    for i in range(0, 11):
        time.sleep(1)  # Sleep for 1 second
        print(10-i)
    print("Liftoff!")
    
if __name__ == "__main__":
    main()