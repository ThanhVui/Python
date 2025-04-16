fruit = 'banana'

index = 0

while index < len(fruit): # When index is less than the length of the string
    # The length of the string is 6, so the index will go from 0 to 5
    letter = fruit[index]
    print(index, letter)
    index += 1

print (" ")

for letter in fruit:
    print(letter)