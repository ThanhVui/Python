# while True:
#     line = input('> ')
#     if line.lower() == 'done':
#         break
#         # Breaks out of loop if done
#         # Otherwise, the loop continues and prints line.
#     print(line)
# print('Done!')


while(line := input('> ')).lower() != 'done':
    print(line)
print('Done!')
# This code is a simple loop that takes user input until the user types 'done'.