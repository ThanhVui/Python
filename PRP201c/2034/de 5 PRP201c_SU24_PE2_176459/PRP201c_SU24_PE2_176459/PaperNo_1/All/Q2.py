def readFromFile(filePath):
    """
    Reads a file and returns a list of lines.
    """
    data = []
    with open(filePath, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                data.append(line)
    return data

def writeToFile(filePath, data):
    """
    Writes a list of lines to a file.
    """
    with open(filePath, 'w') as file:
        for line in data:
            file.write(str(line) + ', ', )

def primeNumbers(data):
    primeList = []
    data = [int(num) for num in data]  # Convert data to integers
    for num in data:
        if num > 1:  # Prime numbers are greater than 1
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):  # Check divisors up to sqrt(num)
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primeList.append(num)
    return primeList
def main(): 
    data = readFromFile(r'integers_data.txt')
    primeList = primeNumbers(data[0].split(' '))
    print("List of integers:", data[0].split(' '))
    print("List of prime numbers:", primeList)
    writeToFile('prime_numbers.txt', primeList)
    print("Prime numbers have been written to 'prime_numbers.txt'.")

if __name__ == "__main__":
    main()