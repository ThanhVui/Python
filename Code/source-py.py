import csv
from collections import defaultdict

#                                                               Handle File
import os

# Ex1 Read File
# f = open("demofile.txt", "r")
# print(f.readline())
# f.close()

# Ex2 Remove File
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")
  
# Ex3 Remove Folder
# os.rmdir("myfolder")



#                                                               Numpy
import numpy as np



#                                                               Pandas
import pandas as pd

# Ex1 Data Frame
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# #load data into a DataFrame object:
# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

# print(df) 

# # #use a list of indexes:
# # print(df.loc[[0, 1]])

# Ex2 Read CSV
# df = pd.read_csv('user_data.csv')

# print(df) 
# # print(df.to_string()) 

# Ex3 Read JSON
# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }
# }

# df = pd.DataFrame(data)

# print(df)

# Ex4 Cleaning Data
# df.loc[7, 'Duration'] = 45
# print(df.duplicated())
# df = df.drop_duplicates()



#                                                               Matplotlib
# pip install matplotlib
import matplotlib.pyplot as plt
# import numpy as np

# Ex1
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, 'o:r', ms = 10, mec = 'r', mfc = 'g', 
#          linewidth=5)

# y1 = np.array([1, 3, 5, 7])
# y2 = np.array([6, 2, 7, 11])

# font1 = {'family':'serif','color':'blue','size':20}
# font2 = {'family':'serif','color':'darkred','size':15}

# plt.title("Sports Watch Data", fontdict = font1, loc = 'left')
# plt.xlabel("Average Pulse", fontdict = font2)
# plt.ylabel("Calorie Burnage", fontdict = font2)

# plt.plot(y1)
# plt.plot(y2)

# plt.grid(axis = 'y', color = 'green', linestyle = '--', linewidth = 0.5)

# plt.show()

# Ex2
# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(1, 2, 1)
# plt.plot(x,y)
# plt.title("SALES")

# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(1, 2, 2)
# plt.plot(x,y)
# plt.title("INCOME")

# plt.suptitle("MY SHOP")
# plt.show()

# Ex3 Bar
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.barh(x, y,  color = "hotpink")
# plt.show()

# Ex4 Histogram
# x = np.random.normal(170, 10, 250)

# plt.hist(x)
# plt.show() 

# Ex5 Pie Charts
# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# myexplode = [0.2, 0, 0, 0]

# plt.pie(y, labels = mylabels, explode = myexplode, shadow = True, startangle = 90)
# plt.legend(title = "Four Fruits:")
# plt.show() 



#                                                               Class
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()



#                                                               SQLite
import sqlite3



#                                                               APIs
# import requests
# try:
#   res = requests.get("https://randomuser.me/api/")
#   if res.status_code == 200:
#     info = res.json()["results"][0]
#     username = info["login"]["username"]
#     picture = info["picture"]["large"]
#     timezone = info["location"]["timezone"]["offset"] + " " + info["location"]["timezone"]["description"]
    
#     print(f"Username: {username}\nPicture URL: {picture}\nTimezone: {timezone}")
# except:
#   print("An error occurred while fetching user data.")