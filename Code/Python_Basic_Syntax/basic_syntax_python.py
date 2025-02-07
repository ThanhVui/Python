# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import sys

# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
    # print data
# print("Hello Word!")
# print(sys.version)

    # if statement
# if 5 > 2:
#     print("That's right!")
# if 5 > 2:
#         print("That's right!")

    # Variable
# x = 5
# y = "Hello, World!"

"""
This is comment
more than one
line
"""
# from itertools import count
# from time import process_time
# from tkinter.font import names

# x = 5
# y = 10
# print("Multiplie: x * y = " + str(x * y))

"""
- in python either use single or double quotes
- in python variable name are case-sensitive (not ignore uppercase or lowercase)
"""
# x = 3
# y = "Vui"
# z = 4
# Z = 39
# print(str(3))
# print(str(y))
# print(float(z))
# print(int(z))
# print(Z)
#
# print(type(x))
# print(type(y))
# print(type(z))

"""
- there are three rules to put name for variable
    + camelCase: myVariable = "Vui"
    + PascalCase: MyVariable = "Vui"
    + SnakeCase: my_variable = "Vui"
"""

"""
assign multiple value
"""
# a, b, c = "Vui", 3, "Happy"
# print(a, b, c)
# print(type(a), type(b), type(c))
#
# x = y = z = "Assign Multiple Value"
# print(x, y, z)

"""
unpack a collection
"""
# fruits = ["apple", "banana", "cherry"]
# e, f, g = fruits
# print(e, f, g)

"""
you can also use the '+' or ',' operator to output multiple values
"""
# x = "Python"
# y = "Is"
# z = "Happy"
# print(x, y, z)
# print(x + " " + y + " " + z)

"""
operator
"""
# x = 4
# y = 3
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x // y) # remainder

# x = 4
# y = "Vui"
# print(x, y)

"""
function print function basic
"""

# def myName(name):
#     print("My name is " + name)
#
# def myFullName(firstName, lastName):
#     print("My full name is " + firstName + " " + lastName)
#
# myName("Vui")
# myName("Happy")
# myFullName("Vui", "Thanh")

"""
global variable
"""
# x = "Thanh Vui"
# def myGlobalVariable():
#     x = "Happy"
#     print(x)
# myGlobalVariable() #"Happy"
# print(x) #"Thanh Vui"

# def myGlobal():
#     global x
#     x = "Thanh Vui"
# myGlobal()
# print(x)

# x = "Thanh Vui"
# def myGlobalVariable():
#     global x
#     x = "Happy"
#     print(x)
# myGlobalVariable() #"Happy"
# print(x) #"Happy"

"""
data types
"""
# x = None
# print(type(x))
# print(x)

# x = 1
# y = 32840924830984092480980943859035803508380958580385903
# z = -3255522
# print(type(x))
# print(type(y))
# print(type(z))

# x = -87.7e100
# print(type(x))# print(x)

# x = 3 + 5j
# print(type(x))
# print(x)

# x = 3.3
# print(int(x))

# import random
# print(random.randrange(1, 5))

# a = '''thanh
# vui
# tang'''
# b = """\nthanh
# vui
# tang"""
# print(a, b)

# a = "Thanh, Vui"
# print(a[3])

# count = 0
# for x in "ThanhVui":
#     # count += 1
#     print(x)
# # print(count)

"""
to get the length of string use len()
"""
# a = "This is a string"
# print(len(a))

"""
check string in sequence
"""
# a = "Thanh Vui Handsome"
# print("Vui" in a)
# if "Vvi" in a:
#     print("Yes, 'Vui' in this text!")
# else:
#     print("No, 'Vui' not in this text!")
#
# if "vui" not in a:
#     print("Yes, 'Vui' not in this text!")
# else:
#     print("No, 'Vui' in this text!")

# a = "Thanh Vui Handsome"
# print(a[-5:-2])

# a = "  Thanh, Vui, Handsome  "
# print(a.upper())
# print(a.lower())
# print(a.strip())
# print(a.replace("Vui", "Happy"))
# print(a.split(", "))

# name = "Vui"
# age = 21
# a = 2
# b = 4
# price = 2.9039082
# txt = f"My name is {name}.\nI'm {age} years old.\n{a * b}\n{price:.3f}"
# print(txt)

# a = "this is a string"
# print(len(a))
# print(a.center(100, " "))
#
#
# txt = "banana"
#
# x = txt.center(20, "O")
#
# print(x)

# print(bool(""))
# print(bool(0))

# a = 200
# print(isinstance(a, int))

"""
operators
"""
# print(3 ** 3) # exponentiation
# print(19 % 3) # modulus
# print(19 // 3) # floor division

# a = 5 # 0101
# b = 3 # 0011
# a &= b # 0001
# print(a) # 0001 = 1
#
# a = 5 # 0101
# b = 3 # 0011
# a |= b # 0111
# print(a) # 0111 = 7
#
# a = 5 # 0101
# b = 3 # 0011
# a ^= b # 0110
# print(a) # 0110 = 6
#
# a = 5 # 0101
# a >>= 2 # 0001
# print(a) # 0001 = 1
#
# a = 5 # 0101
# a <<= 2 # 0100
# print(a) # 01 0100 = 4


"""
list
"""
# there is two ways to create a list use ["java", "python", 12] or list(("java", "python", 12))
# myList = ["java", "python", 12]
# print(type(myList))
#
# myList = ["java", "python", 12, "dart", "javascript", "kotlin"]
# print(myList[3])
# print(myList[-1])
# print(myList[-2])
# print(myList[2:4])

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "mango")
# thislist.append("orange")
# print(thislist)

# thisList = ["apple", "banana", "cherry"]
# thatList = ["mango", "orange", "lemon"]
# thatList.extend(thisList)
# print(thatList)

# thisList = ["apple", "banana", "cherry"]
# thatList = ("mango", "orange", "lemon")
# thisList.extend(thatList)
# print(thisList)

# thislist = ["apple", "banana", "cherry"]
# # thislist.remove("banana")
# # thislist.pop(0)
# # del thislist[2]
# # del thislist
# # thislist.clear()
# # print(thislist)
# print(range(len(thislist)))
# # for item in range(len(thislist)):
# #     print(thislist[item])

# thislist = ["apple", "banana", "cherry"]
# # i = 0
# # while i < len(thislist): # 1 < 3 (0, 1, 2)
# #     print(thislist[i])
# #     i += 1
#
# [print(x) for x in thislist]

"""
list comprehension
"""
# thatList = ["mango", "orange", "lemon"]
# newList = []
# for x in thatList:
#     if "a" in x:
#         newList.append(x)
#
# print(newList)

# short hand
# thatList = ["mango", "orange", "lemon"]
# newList = [x for x in thatList if "a" in x]
# print(newList)

# newList = [x for x in range(10)]
# print(newList)

# newList = [x for x in range(10) if x > 3]
# print(newList)

# thatList = ["mango", "orange", "lemon"]
# newList = [x.upper() for x in thatList]
# print(newList)

# thatList = ["mango", "orange", "lemon"]
# newList = ["Vui" for x in thatList]
# print(newList)

# thatList = ["mango", "orange", "lemon"]
# newList = [x if x != "mango" else "apple" for x in thatList]
# print(newList)

# thatList = ["mango", "orange", "lemon"]
# thatList.sort()
# print(thatList)

# numList = [2, 1, 7, 3, 6, 5, 0]
# numList.sort()
# print(numList)

# numList = [2, 1, 7, 3, 6, 5, 0]
# numList.sort(reverse = True)
# print(numList)

# def myfunc(n):
#   return abs(n - 50)
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)  # 50, 0, 15, 32, 27
# print(thislist) # 50, 65, 23, 82, 100

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.reverse()
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# newList = thislist.copy()
# print(newList)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# newList = thislist[:]
# print(newList)

"""
tuple
"""
# myTuple = ("apple", "banana", "cherry")
# firstTuple = ("apple",)
# tuple2 = tuple(("apple", "banana", "cherry"))
# print(myTuple)

# convert from tuple to list and convert list to tuple to change tuple
# tuple1 = ("apple", "banana", "cherry")
# list1 = list(tuple1)
# list1[2] = "mango"
# tuple1 = tuple(list1)
# print(tuple1)

# add items into tuple
# tuple1 = ("apple", "banana", "cherry")
# list1 = list(tuple1)
# list1.append("mango")
# tuple1 = tuple(list1)
# print(tuple1)

# add tuple to tuple
# tuple1 = ("apple", "banana", "cherry")
# tuple2 = ("mango",)
# tuple1 += tuple2
# print(tuple1)

# remove items in tuple
# tuple1 = ("apple", "banana", "cherry")
# list1 = list(tuple1)
# list1.remove("apple")
# tuple1 = tuple(list1)
# print(tuple1)

# unpacking a tuple
# tuple1 = ("apple", "banana", "cherry")
# (item1, item2, item3) = tuple1
# print(item1)
# print(item2)
# print(item3)

# tuple1 = ("apple", "banana", "cherry", "mango")
# (item1, item2, *item3) = tuple1
# print(item1)
# print(item2)
# print(item3)

# tuple1 = ("apple", "banana", "cherry", "mango")
# (item1, *item2, item3) = tuple1
# print(item1)
# print(item2)
# print(item3)

# loop tuple
# tuple1 = ("apple", "banana", "cherry", "mango")
# for item in tuple1:
#     print(item)

# loop use rang and len
# tuple1 = ("apple", "banana", "cherry", "mango")
# for item in range(len(tuple1)):
#     print(tuple1[item])

# while loop
# tuple1 = ("apple", "banana", "cherry", "mango")
# item = 0
# while item < len(tuple1):
#     print(tuple1[item])
#     item += 1

# join two tuple
# tuple1 = ("apple", "banana", "cherry", "mango")
# tuple2 = ("lemon",)
# tuple3 = tuple1 + tuple2
# print(tuple3)

# tuple1 = ("apple", "banana", "cherry", "mango")
# tuple2 = tuple1 * 2
# print(tuple2)


"""
sets
"""
# mySets = {"apple", "banana", "cherry"}
# print(mySets)
#
# set1 = set(("apple", "banana", "cherry", True, 1, "apple", False, 0))
# print(set1)

# mySets = {"apple", "banana", "cherry"}
# mySets.add("mango")
# print(mySets)

# mySets = {"apple", "banana", "cherry"}
# sets2 = {"pineapple", "mango", "lemon"}
# mySets.update(sets2)
# print(mySets)

# mySets = {"apple", "banana", "cherry"}
# sets2 = ["pineapple", "mango", "lemon"]
# mySets.update(sets2)
# print(mySets)

# mySets = {"apple", "banana", "cherry"}
# mySets.remove("banana")
# print(mySets)

# mySets = {"apple", "banana", "cherry"}
# mySets.discard("banana")
# print(mySets)

# mySets = {"apple", "banana", "cherry"}
# x = mySets.pop()
# print(x)
# print(mySets)

# mySets = {"apple", "banana", "cherry"}
# mySets.clear()
# print(mySets)

# mySets = {"apple", "banana", "cherry"}
# for item in mySets:
#     print(item)


# sets1 = {"apple", "banana", "cherry"}
# sets2 = {"pineapple", "mango", "lemon"}
# sets3 = {"orange",}
# sets4 = {"nana"}
# sets5 = sets1.union(sets2, sets3, sets4)
# print(sets5)

# sets1 = {"apple", "banana", "cherry"}
# sets2 = {"pineapple", "mango", "lemon"}
# sets3 = {"orange",}
# sets4 = {"nana"}
# sets3 = sets1 | sets2 | sets3 | sets4
# print(sets3)

# sets1 = {"apple", "banana", "cherry"}
# sets2 = {"pineapple", "mango", "lemon"}
# sets3 = {"orange",}
# sets4 = {"nana", "banana", "cherry"}
# sets5 = sets1.intersection(sets4)
# print(sets5)

# sets1 = {"apple", "banana", "cherry"}
# sets2 = {"pineapple", "mango", "lemon"}
# sets3 = {"orange",}
# sets4 = {"nana", "banana", "cherry"}
# sets5 = sets1 & sets4
# print(sets5)

# sets1 = {"apple", "banana", "cherry"}
# sets2 = {"banana", "mango", "lemon"}
# sets5 = sets1.intersection_update(sets2)
# print(sets5)

# sets1 = {"apple", "banana", "cherry"}
# sets2 = {"banana", "mango", "lemon"}
# sets5 = sets1.difference(sets2)
# print(sets5)

# sets1 = {"apple", "banana", "cherry"}
# sets2 = {"banana", "mango", "lemon"}
# sets5 = sets1 - sets2
# print(sets5)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.difference_update(set2)
# print(set1)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2)
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 ^ set2
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.symmetric_difference_update(set2)
# print(set1)

"""
dictionaries
"""
# dict1 = {
#     "brand": "ford",
#     "model": "Mustang",
#     "year": 1999
# }
# print(dict1)

# get the value of key through [key]
# dict1 = {
#     "brand": "ford",
#     "model": "Mustang",
#     "year": 1999
# }
# print(dict1["model"])

# dict1 = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
# print(dict1)

# dict use dict()
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# print(dict1)

# how to get value from key
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# x = dict1.get("name")
# print(x)

# how to get key from value
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# x = dict1.keys()
# print(x)

# how to change
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# x = dict1.keys()
# print(x)
# dict1["color"] = "red"
# print(x)

# how to change
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# x = dict1.values()
# print(x)
# dict1["color"] = "red"
# print(x)

# how to change
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# x = dict1.items()
# print(x)
# dict1["color"] = "red"
# print(x)

# how to change value of key
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# dict1["name"] = "Happy"
# print(dict1)

# how to change value of key
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# dict1.update({"name": "Happy"})
# print(dict1)

# how to change value of key
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# dict1.pop("name")
# print(dict1)

# how to change value of key
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# dict1.pop("name")
# print(dict1)

# how to remove item
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)

# how to loop through dict
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# for item in dict1:
#     print(dict1[item])

# how to loop through dict
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# for item in dict1.values():
#     print(item)

# how to loop through dict
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# for item in dict1.keys():
#     print(item)

# how to loop through dict
# dict1 = dict(name = "Vui", age = 21, country = "United Kingdom")
# for key, value in dict1.items():
#     print(key, value)

"""
nested dictionary
"""
# mydict = {
#     "dict1": {
#         "name": "John",
#         "age": 30
#     },
#     "dict2": {
#         "name": "Vui",
#         "age": 33
#     },
#     "dict3": {
#         "name": "Happy",
#         "age": 22
#     }
# }
# print(mydict)

# dict into dict
# dict1 = {
#     "name": "John",
#     "age": 30
# }
# dict2 = {
#     "name": "Vui",
#     "age": 33
# }
# dict3 = {
#     "name": "Happy",
#     "age": 22
# }
#
# mydict = {
#     "child1": dict1,
#     "child2": dict2,
#     "child3": dict3
# }
# print(mydict)

# dict1 = {
#     "name": "John",
#     "age": 30
# }
# dict2 = {
#     "name": "Vui",
#     "age": 33
# }
# dict3 = {
#     "name": "Happy",
#     "age": 22
# }
#
# mydict = {
#     "child1": dict1,
#     "child2": dict2,
#     "child3": dict3
# }
# print(mydict["child1"]["name"])

# dict1 = {
#     "name": "John",
#     "age": 30
# }
# dict2 = {
#     "name": "Vui",
#     "age": 33
# }
# dict3 = {
#     "name": "Happy",
#     "age": 22
# }
#
# mydict = {
#     "child1": dict1,
#     "child2": dict2,
#     "child3": dict3
# }
# for item, object in mydict.items():
#     print(item)
#     for child in object:
#         print(item + ":", object[child])

"""
if else statement
if
elif
else
"""
# a = 3
# b = 3
# if a > b:
#     print("a greater than b")
# elif a < b:
#     print("a less than b")
# else:
#     print("a equals b")
#
# if a == b: print("a equals b")

# a = 3
# b = 3
# print("a equal b") if a == b or a < b else print("not equal")

# a = 3
# b = 2
# if b < a:
#     print(a)
#     pass

"""
while and for loop
"""
# i = 1
# while i < 6:
#     print(i)
#     i += 1
#
# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# i = 1
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("i is no longer less than 6")

# for x in range(6):
#     print(x)

# for x in range(2, 6):
#      print(x)

# for x in range(2, 30, 3):
#      print(x)
# else:
#     print("Finally For Loop")


"""
function
"""
# def function1():
#     print("Hello World")
# function1()
# function1()

# def my_function(*kids):
#   for x in kids:
#       print("The youngest child is " + x)
#
# my_function("Emil", "Tobias", "Linus")
#
# def my_function(**kid):
#   print("His last name is " + kid["fname"])
#
# my_function(fname = "Tobias", lname = "Refsnes")
#
# def my_function(country = "Norway"):
#   print("I am from " + country)
#
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")
#
# from torchvision.datasets import ImageFolder
# import torch
#
# dataset = ImageFolder()
"""Python Programing For Everybody"""
"""======================================================================"""
"""Read file and count number of word in file txt"""
# name = input("Enter file: ") # Input name of file
# handle = open(name) # Open file with name input
# counts = dict() # Create a dictionary to store count of word
# for line in handle: # Read line by line
#     words = line.split() # Split word into each line
#     for word in words: # Loop through each words to take word and store it into dict counts
#         counts[word] = counts.get(word, 0) + 1
#
# bigcount = None # Create bigcount
# bigword = None # Create bigword
# for word, count in counts.items(): #
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count
#
# print(bigword, bigcount)
"""======================================================================"""
"""Read file and count number of word in file txt"""
# fileword = open('words.txt', 'r')
# counts = 0
# for line in fileword:
#     print(line.strip())
#     counts += 1
# print(counts, "Lines")
"""======================================================================"""
"""Basic Python"""
# hrs = input("enter hours:")
# rate = input("enter rate:")
# try:
#     h = float(hrs)
#     r = float(rate)
# except:
#     print("Error convert h or r to float")
#     quit()
"""======================================================================"""
"""Open File"""
# fhand = open('words.txt', 'r')
# print(fhand.read())
"""======================================================================"""
# """Counting Pattern"""
# counts = dict()
# print(" Enter a line of text:")
# line = input('')
# words = line.split()
# print("Words:", words)
# print("Counting...")
# for word in words:
#     counts[word] = counts.get(word, 0) + 1
# print("Counts:", counts)

# stuff = dict()
# print(stuff['candy'])

# stuff = dict()
# print(stuff.get('candy',-1))


# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
# Asking user to enter the source file
# fname = input("Enter file:")
# if len(fname) < 1 : fname = "mbox-short.txt"
# # Opening the source file
# fhandle = open(fname)

# # Creating a dictionary for the hours
# hours = dict()

# # Reading file line-by-line
# for line in fhandle:
#     line.rstrip()
#     # Looking for lines starting with 'From'
#     if line.startswith('From ') :
#         # Splitting lines starting with 'From'
#         ls = line.split()
#         # Taking the split with the time
#         time = ls[5]
#         # Splitting the time
#         tm = time.split(':')
#         # Taking the split with the hour
#         hour = tm[0]
#         # Adding the hour in the dictionary and counting
#         hours[hour] = hours.get(hour, 0) + 1

# # Printing the hours and their counts in ascending order by hours
# for k,v in sorted(hours.items()):
#     print(k,v)


#Finding Numbers in a Haystack

#In this assignment you will read through and parse a file with text and numbers.
#You will extract all the numbers in the file and compute the sum of the numbers.

#Data Files
#We provide two files for this assignment.
#One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
#Actual data: http://py4e-data.dr-chuck.net/regex_sum_38794.txt (There are 90 values and the sum ends with 360)

#The basic outline of this problem is to read the file, look for integers using the re.findall(),
#looking for a regular expression of '[0-9]+'
#and then converting the extracted strings to integers and summing up the integers.

# import re
# name = input("Enter file:")
# if len(name) < 1 : name = "test.txt"
# fh = open(name)
# newlist = list()
# for line in fh :
#     line = re.findall('[0-9]+', line)  #finds all numbers '.[0-9]*[0-9]' was before and it missed py4e.com and etx
#     for number in line :
#         newlist.append(int(number)) # creates newlist with int line values
# print(sum(newlist))


## supershort print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )


#Exploring the HyperText Transport Protocol

#You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.

#http://data.pr4e.org/intro-short.txt
#There are three ways that you might retrieve this web page and look at the response headers:

#Preferred: Modify the socket1.py program to retrieve the above URL and print out the headers and data.
#Make sure to change the code to retrieve the above URL - the values are different for each URL.
#Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned.
#Use the telnet program as shown in lecture to retrieve the headers and content.
#Enter the header values in each of the fields below and press "Submit".

# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if (len(data) < 1):
#         break
#     print(data.decode())
# mysock.close()

#Scraping Numbers from HTML using BeautifulSoup.
#In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py.
#The program will use urllib to read the HTML from the data files below,
#and parse the data, extracting numbers and compute the sum of the numbers in the file.


#The file is a table of names and comment counts. You can ignore most of the data in the file except for lines like the following:

#<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
#<tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
#<tr><td>Hubert</td><td><span class="comments">87</span></td></tr>
#You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
#Look at the sample code provided. It shows how to find all of a certain kind of tag, loop through the tags and extract the various aspects of the tags.

...
# Retrieve all of the anchor tags
#tags = soup('a')
#for tag in tags:
   # Look at the parts of a tag
 #  print 'TAG:',tag
  # print 'URL:',tag.get('href', None)
   #print 'Contents:',tag.contents[0]
   #print 'Attrs:',tag.attrs
#You need to adjust this code to look for span tags and pull out the text content of the span tag, convert them to integers and add them up to complete the assignment.
#Sample Execution

#$ python3 solution.py
#Enter - http://py4e-data.dr-chuck.net/comments_42.html
#Count 50
#Sum 2...


# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

#Actual data: http://py4e-data.dr-chuck.net/comments_38796.html (Sum ends with 87)

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# html = urlopen(url, context=ctx).read()

# # html.parser is the HTML parser included in the standard Python 3 library.
# # information on other HTML parsers is here:
# # http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
# soup = BeautifulSoup(html, "html.parser")
# sumnum = list()
# # Retrieve all of the anchor tags
# tags = soup('span')
# for tag in tags:
#     # Look at the parts of a tag (just for fun)
#     print('TAG:', tag)
#     print('URL:', tag.get('href', None))
#     print('Contents:', tag.contents[0])
#     print('Attrs:', tag.attrs)
#     x = tag.contents[0]
#     sumnum.append(int(x))
# print(sum(sumnum))


# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# counts = dict()
# for line in fhand:
#     words = line.decode().split()
#     for word in words:
#         counts [word] = counts.get(word, 0)+1
# print(counts)


#Scraping Numbers from HTML using BeautifulSoup.
#In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py.
#The program will use urllib to read the HTML from the data files below,
#and parse the data, extracting numbers and compute the sum of the numbers in the file.


#The file is a table of names and comment counts. You can ignore most of the data in the file except for lines like the following:

#<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
#<tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
#<tr><td>Hubert</td><td><span class="comments">87</span></td></tr>
#You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
#Look at the sample code provided. It shows how to find all of a certain kind of tag, loop through the tags and extract the various aspects of the tags.

...
# Retrieve all of the anchor tags
#tags = soup('a')
#for tag in tags:
   # Look at the parts of a tag
 #  print 'TAG:',tag
  # print 'URL:',tag.get('href', None)
   #print 'Contents:',tag.contents[0]
   #print 'Attrs:',tag.attrs
#You need to adjust this code to look for span tags and pull out the text content of the span tag, convert them to integers and add them up to complete the assignment.
#Sample Execution

#$ python3 solution.py
#Enter - http://py4e-data.dr-chuck.net/comments_42.html
#Count 50
#Sum 2...


# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

#Actual data: http://py4e-data.dr-chuck.net/comments_38796.html (Sum ends with 87)

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# html = urlopen(url, context=ctx).read()

# # html.parser is the HTML parser included in the standard Python 3 library.
# # information on other HTML parsers is here:
# # http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
# soup = BeautifulSoup(html, "html.parser")
# sumnum = list()
# # Retrieve all of the anchor tags
# tags = soup('span')
# for tag in tags:
#     # Look at the parts of a tag (just for fun)
#     print('TAG:', tag)
#     print('URL:', tag.get('href', None))
#     print('Contents:', tag.contents[0])
#     print('Attrs:', tag.attrs)
#     x = tag.contents[0]
#     sumnum.append(int(x))
# print(sum(sumnum))


#Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Bailley.html
#Find the link at position 18 (the first name is 1). Follow that link.
#Repeat this process 7 times. The answer is the last name that you retrieve.
#Hint: The first character of the name of the last page that you will load is: I

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# html = urlopen(url, context=ctx).read()

# soup = BeautifulSoup(html, "html.parser")

# # Retrieve all of the anchor tags
# tags = soup('a')

# position = input('Enter position: ')
# position = int(position)
# position = position - 1 # to take into account 0,1,2 ...
# count = input('Enter count: ') # desired amount of cycle repetitions
# count = int(count)

# meter = 0 # for 0 repetitions of the cycle
# meter = int(meter)

# while count != meter :

#     print('TAG:', tags[position])
#     print('URL:', tags[position].get('href', None))
#     print('Contents:', tags[position].contents[0])
#     print('Attrs:', tags[position].attrs)
#     meter = meter + 1

#     ctx = ssl.create_default_context()
#     ctx.check_hostname = False
#     ctx.verify_mode = ssl.CERT_NONE

#     url = tags[position].get('href', None)
#     print(url)
#     html = urlopen(url, context=ctx).read()
#     soup = BeautifulSoup(html, "html.parser")
#     tags = soup('a')
#     print('break', meter, count)


#Extracting Data from XML

#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py.
#The program will prompt for a URL, read the XML data from that URL using urllib and then parse
#and extract the comment counts from the XML data, compute the sum of the numbers in the file.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_38798.xml (Sum ends with 55)

#<comment>
  #<name>Matthias</name>
  #<count>97</count>
#</comment>
#You are to look through all the <comment> tags and find the <count> values sum the numbers.
#The closest sample code that shows how to parse XML is geoxml.py.
#But since the nesting of the elements in our data is different than the data we are parsing
#in that sample code you will have to make real changes to the code.
#To make the code a little simpler, you can use an XPath selector string to
#look through the entire tree of XML for any tag named 'count' with the following line of code:

#counts = tree.findall('.//count')
#Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details.
#You could also work from the top of the XML down to the comments node and then loop through the child nodes of the comments node.

# import urllib.request, urllib.parse, urllib.error
# import xml.etree.ElementTree as ET

# url = input('Enter - ')
# print('1_Retrieving', url, type(url)) #class str
# uh = urllib.request.urlopen(url)
# print('2_uh', uh, type(uh)) #class 'http.client.HTTPResponse'
# data = uh.read()
# print("3_uh.read() or data", data, type(data)) #calss bytes
# data = data.decode()
# print("4_data decode", data, type(data)) #class str
# tree = ET.fromstring(data)
# print("5_tree", tree, type(tree)) #class 'xml.etree.ElementTree.Element'
# count = tree.findall('.//count')
# print("6_count", count, type(count), "len", len(count)) #class 'list
# i = 0
# i = int(i)
# sumnum = list()
# while True :
#     try :
#         countext = count[i].text
#         countext = int(countext)
#         sumnum.append(countext)
#         print("7_count", countext, type(countext))
#         i = i + 1
#         continue
#     except :
#         break
# print("sumnum", sum(sumnum), type(sumnum))


#Extracting Data from JSON

#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py.
#The program will prompt for a URL, read the JSON data from that URL using urllib and then parse
#and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
#We provide two files for this assignment.
#One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_38799.json (Sum ends with 87)

#You do not need to save these files to your folder since your program will read the data directly from the URL.
#Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
#Data Format
#The data consists of a number of names and comment counts in JSON as follows:

#The closest sample code that shows how to parse JSON and extract a list is json2.py.
#You might also want to look at geoxml.py to see how to prompt for a URL and retrieve data from a URL.

# import json
# import urllib.request, urllib.parse, urllib.error

# url = input('Enter - ')
# print('1_Retrieving', url, type(url)) #class str
# uh = urllib.request.urlopen(url)
# print('2_uh', uh, type(uh)) #class 'http.client.HTTPResponse'
# data = uh.read()
# print("3_uh.read() or data", data, type(data)) #calss bytes
# data = data.decode()
# print("4_data decode", data, type(data)) #class str
# info = json.loads(data)
# print("5_info", info, type(info), '5_len_info', len(info)) #class dict
# print('6_comments',info['comments'][2]['count']) # just as way to recover smth
# print('7_comments type', type(info['comments']), '7_comments len', len(info['comments']))
# x = 0
# for item in (info['comments']) :
#     print('count', item['count'], type(item['count']))
#     x = x + item['count']
# print(x)


#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py.
#The program will prompt for a location, contact a web service and retrieve JSON for the web service
#and parse that data, and retrieve the first place_id from the JSON.
#A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
#API End Points

#To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

#http://py4e-data.dr-chuck.net/geojson?
#This API uses the same parameters (sensor and address) as the Google API. This API also has no rate limit so you can test as often as you like.
#If you visit the URL with no parameters, you get a list of all of the address values which can be used with this API.
#To call the API, you need to provide address
#that you are requesting as the address= parameter
#that is properly URL encoded using the urllib.urlencode() fuction as shown in http://www.py4e.com/code3/geojson.py

#Test Data / Sample Execution

#You can test to see if your program is working with a location of "South Federal University"
#which will have a place_id of "ChIJJ8oO7_B_bIcR2AlhC8nKlok".

#Please run your program to find the place_id for this location:

#Banaras Hindu University
#Make sure to enter the name and case exactly as above and enter the place_id and your Python code below.
#Hint: The first seven characters of the place_id are "ChIJqSi ..."
#Make sure to retreive the data from the URL specified above and not the normal Google API.
#Your program should work with the Google API - but the place_id may not match for this assignment.

# import urllib.request, urllib.parse, urllib.error
# import json

# # Note that Google is increasingly requiring keys
# # for this API
# serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

# while True:
#     address = input('Enter location: ')
#     if len(address) < 1: break

#     url = serviceurl + urllib.parse.urlencode(
#         {'address': address})

#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url)
#     data = uh.read().decode()
#     print('Retrieved', len(data), 'characters')

#     try:
#         js = json.loads(data)
#     except:
#         js = None

#     if not js or 'status' not in js or js['status'] != 'OK':
#         print('==== Failure To Retrieve ====')
#         print(data)
#         continue

#     print(json.dumps(js, indent=4))

#     lat = js["results"][0]["geometry"]["location"]["lat"]
#     lng = js["results"][0]["geometry"]["location"]["lng"]
#     print('lat', lat, 'lng', lng)
#     location = js['results'][0]['formatted_address']
#     print(location)


# import urllib.parse
# import urllib.request
# import json

# # Correct API Endpoint
# api_url = "http://py4e-data.dr-chuck.net/opengeo?"

# # Input location
# location = input("Enter location: ")

# # Encode location into URL format
# params = {"q": location}
# url = api_url + urllib.parse.urlencode(params)

# # Retrieve data from API
# print("Retrieving", url)
# response = urllib.request.urlopen(url)
# data = response.read().decode()

# print("Retrieved", len(data), "characters")

# # Parse JSON
# try:
#     json_data = json.loads(data)
    
#     # Print full JSON response for debugging
#     print(json.dumps(json_data, indent=4))

#     # Check if 'features' exist and extract properties
#     if "features" in json_data and len(json_data["features"]) > 0:
#         properties = json_data["features"][0]["properties"]
        
#         # Print all available fields to find the plus_code
#         print("Properties:", json.dumps(properties, indent=4))

#         # If plus_code exists, extract it
#         if "plus_code" in properties:
#             plus_code = properties["plus_code"]
#             print("Plus code:", plus_code)
#         else:
#             print("No plus code found in properties.")
#     else:
#         print("No valid location data found.")
# except json.JSONDecodeError:
#     print("Error parsing JSON response")
