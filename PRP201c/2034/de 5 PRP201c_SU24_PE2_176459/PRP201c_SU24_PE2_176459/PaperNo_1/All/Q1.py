import random


def getInteger(promt , min = None): 
    while True: 
        try : 
            value = int(input(promt))
            if min is not None or value > min : 
                return value
            else :
                print(f"Please enter a number greater than {min}.")

        except ValueError: 
            print("Please enter a valid integer.")
            continue

def main() : 
    start = getInteger("Enter a start of the range : ", 0)
    end = getInteger("Enter an end of the range : ", start)

    numberWantToCreate = getInteger("Enter the number of random numbers you want to create : ", 0)
    randomNumbers = set() 

    if numberWantToCreate > (end - start + 1) : 
        print("The number of random numbers you want to create is greater than the range.")
        return

    while len(randomNumbers) < numberWantToCreate : 
        randomNumbers.add(random.randint(start, end))

    print("Generated list of unique integers" , randomNumbers)
    
    numberOfEven = sum(1 for num in randomNumbers if num % 2 == 0)
    numberOfOdd = sum(1 for num in randomNumbers if num % 2 != 0)
    print("Number of even numbers : " , numberOfEven)
    print("Number of odd numbers : " , numberOfOdd)
    
if __name__ == "__main__" : 
    main()