found = False

print(f'Before {found}') # It will print 'Before False'
# This code initializes a boolean variable `found` to `False`, then iterates through a list of numbers.

for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
        break
    print(found, value)

print('After', found)