import random

def main():
            
    print("Enter an integer number of total :" ,end ="")
    total = int(input())
    print("\nDice Thrower")
    print("====================")

    currentTotal = total -1; 
    count = 0
    while currentTotal != total : 
        count += 1
        r1 = random.randint(1, 6)
        r2 = random.randint(1, 6)
        print(f"Result of throw: {count}  {r1} + {r2}")
        currentTotal = r1 + r2

    print (f"You got your total in {count} throws")



if __name__ == "__main__":
    main()