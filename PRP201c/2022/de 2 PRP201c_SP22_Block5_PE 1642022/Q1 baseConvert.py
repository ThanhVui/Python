
import sys

def dec_to_bin(n):
    output = ""
    if n > 1 : 
        while n > 0 : 
            output = str(n%2) + output 
            n = n // 2
    return output

def main():
        
    while True : 
        try:
            number = int(input("Enter a positive integer number: "))
            if number < 1: 
                print("The number must be positive.")
            elif number >= 1 :
                print(f"{number} is converted into binary: {dec_to_bin(number)}")
                break

        except ValueError:
            print("Invalid input. Please enter a positive integer.")
            continue


if __name__ == "__main__":
    main()