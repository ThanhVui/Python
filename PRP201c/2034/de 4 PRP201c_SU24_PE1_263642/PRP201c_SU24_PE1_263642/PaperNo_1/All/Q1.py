
import random


def getInteger(prompt, min=None):
    while True:
        print(prompt, end='')
        try:
            value = int(input())
            if min is None or value >= min:
                return value
            else:
                print('Please enter a number greater than or equal to {}.'.format(min))
        except ValueError:
            print('Invalid input. Please enter an integer.')
def main(): 
    start = getInteger('Enter the start of the range : ')
    end = getInteger('Enter the end of the range : ', start)
    numberOfUniqueNumber = getInteger('Enter the number of unique numbers to generate : ', 0)

    if numberOfUniqueNumber > (end - start + 1):
        print('The number of unique numbers to generate is greater than the range.')
        return
    else : 
        listNumber = random.sample(range(start, end + 1), numberOfUniqueNumber)
        print('Generated list of unique numbers is : ', listNumber)
        print("Average of the integers: ", sum(listNumber) / len(listNumber))
        print("Minium value in the list :", min(listNumber))


if __name__ == "__main__":
    main()