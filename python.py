# getting started
print("Hello, World!")

# syntax
if 5 > 2:
    print("Five is greater than two")

# Variables
x = 23
y = 45
print(x + y)

a = "python "
b = "is "
c = "awesome"
print(a + b + c)

u = "I like "
j = "Codding "
k = "with python language"
print(u + j + k)

# python numbers and strings
h = "Welcome to eMobilis College"
s = 2
d = 2.8
y = 3j
print(type(s))
print(type(d))
print(type(y))
# Counting of the characters in a statement
print(len(h))
# To print all the characters on lower case and upper case
print(h.lower())
print(h.upper())

# Working with Operators
peter = 23 + 23
jack = 46
print(jack is peter)

o = ["Ian", "Dylan","Andrew", "Kevin"]
print("Paul" in o)


thistuple = tuple(("apple", "banana", "cherry"  ))
print(len(thistuple))

# Conditional statements
zulu = 45
south = 45
if zulu < south:print("zulu is less than south")
elif zulu == south:
  print("zulu and south are equal")
else:print("south is greater than zulu")

#  While loops (While loops and for loops)
peter = 1
while peter < 23:
    print(peter)
    peter +=1


jack < 5
while jack < 5:
    jack +=1
    print(jack)

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# for loop
noise_makers = ["Ian","Zeff" , "Paul" , "Peter" , "Reuben" , "Kevin" , "Chairman" , "Temmy"]
for n in noise_makers:
    print(n)
# done to print a lis tof decimal numbers
for s in range(4):
    print(s)

# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
from datetime import time

principle = 2333333
rate = 12.5
time = 2.5
simple_interest = (principle * rate * time)/100
print(simple_interest)

# Python functions
def my_function():
  print("Hello from a function")

my_function()

# Usage of parameters under python function
# Parameters are specified after the function name, inside the parentheses.
# You can add as many parameters as you want, just separate them with a comma.
def my_function(fname):
  print(fname + " Refsnes")

my_function("Reuben")
my_function("Oluyali")
my_function("Omolo")

# using default parameter value
# Example one
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
# Example two
def my_function(food = "Ugali|kuku"):
    print("I like eating " + food)
my_function("Pilau|beef")
my_function()
my_function("Kunde|Ugali")
my_function("Rice|beans")

# using of function to return a value
def my_function(p):
    return 7 * p
print(my_function(34))
print(my_function(23))
print(my_function(3))
print(my_function(5))
print(my_function(87))

# Python lambda
x = lambda a: a + 10
print(x(45))

p = lambda w, q, r: w + q + r
print(p(10, 12, 23))

# Using lambda  as an anonymous function
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(2)

print(mytripler(12))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(3)

print(mydoubler(12))
# When bot of the functions are combined
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(12))
print(mytripler(12))

# Python Arrays
food = ["ugali", "rice", "chicken"]
# printing a specific item in a list
f = food[2]

print(f)
# counting of items in a list
x = len(food)
print(x)

# append function is used in adding an element to an array
atire = ["shoes", "Uniform", "socks", "sweater"]
atire.append("wind_breker")
print(atire)
# Use of pop() function in removal of array elements(used to pop out a decimal number)
atire.pop(1)
print(atire)
# remove function may also be used simultaneously as pop() function i.e.(used to remove letters)
atire.remove("sweater")
print(atire)

# Usage of various elements in python in a list to enable quick formatting
# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list


# python classes and objects
class MyClass:
  x = 45
p1 = MyClass()
print(p1.x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Oluyali", 19)
p2 = Person("Reuben", 22)
p3 = Person("Omolo", 135)
p4 = Person("Penalope", 18)
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)
print(p3.name)
print(p3.age)
print(p4.name)
print(p4.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# python modules
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Reuben", 19)
p1.myfunc()

import mymodule

mymodule.greeting("penalope")
import mymodule

a = mymodule.person1["age"]
print(a)

import platform

x = platform.system()
print(x)

import platform

x = dir(platform)
print(x)


# python datetime
import datetime

x = datetime.datetime.now()

print(x)

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.time())
print(x.strftime("%A"))

# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------

# python JSON(JavaScript object notation)
import json

# some JSON:
x = '{ "name":"Reuben", "age":19, "city":"Jamaica"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# converting from python to JSON
import json

# a Python object (dict):
x = {
  "name": "Reuben",
  "age": 19,
  "city": "Jamaica"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

import json
# Converting Python objects into JSON strings, and printing of the values
print(json.dumps({"name": "Reuben", "age": 19}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


# Convert a Python object containing all the legal data types:
import json

x = {
  "name": "Penalope",
  "age": 18,
  "married": True,
  "divorced": False,
  "children": ("Peninah","Beckham"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

import json
# formatting the result so as to make the list easier to read
x = {
  "name": "Penalope",
  "age": 18,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:(in asorted manner)
print(json.dumps(x, indent=4, sort_keys=True))

# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------

# python file handling in python programming
# Some of the things to note about file handling
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# f = open("myfile.txt", "x")
# g = open("demofile.txt", "a")
# h = open("demofile.txt", "w")
# i = open("myfile.txt", "r")
# j = open("demofile.txt.txt", "b")
# k = open("myfile.txt", "t")


import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exists")


