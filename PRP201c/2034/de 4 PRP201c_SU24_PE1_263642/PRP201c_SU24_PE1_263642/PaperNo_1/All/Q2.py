def readFromFile(fileName):
    data = []
    with open(fileName, "r") as fileObject : 
        for line in fileObject : 
            data.append(line.strip())
    return data

def writeToFile(fileName, data):
    with open(fileName, "w") as fileObject : 
        for line in data : 
            fileObject.write(str(line) + " ")


def main(): 
    listNumber = readFromFile(r"integers_data.txt")
    print("Content of input file {intergers_data.txt}: ", listNumber)

    listEnvenNum = [int(num) for line in listNumber for num in line.split() if int(num) % 2 == 0]
    writeToFile("even_integers.txt", listEnvenNum)
    print("Content of output file {even_integers.txt}: ", listEnvenNum)


if __name__ == "__main__":
    main()