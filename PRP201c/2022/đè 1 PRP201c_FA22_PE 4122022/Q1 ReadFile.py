def main():
        
    fileName = input("Enter file: ")
    if(fileName == ""):
        fileName = r"D:\Ki 5\PRP201c\PRP201c_FA22_PE 4122022\Text.txt"

    listFromFile = []
    listAllCombination = []
    try:
        with open(fileName, "r") as fileObject: 
            # bắt đầu đọc nội dung của file 
            content = fileObject.read() 
            # in nội dung của file
            print(content)
            listFromFile = content.split(",")
    except FileNotFoundError:
        print("File not found")
        exit(1)

    # Combination 

    for i in range(0, len(listFromFile) - 1  , 1 ) : 
        for j in range(i + 1, len(listFromFile), 1):  
            listAllCombination.append(listFromFile[i] + listFromFile[j] + " ")

    print(f"All numbers combinations : {listAllCombination}")
        


if __name__ == "__main__":
    main()