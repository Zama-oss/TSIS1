#Python syntax
#Ex1
print("Hello,world!")

#Ex2
if 5 > 2:
    print("Five is greater than two!")

#Comments

`#Ex1
#This is comment

#Ex2
"""
This is a comment
written in 
more that just one line
"""

#Variables
#Ex1
carname = "Volvo"

#Ex2
x = 50

#Ex3

x = 5
y = 10

print(x + y)

#Ex4
x = 5
y = 10
z = x + y

print(z)

#Ex5

myfirst_name = "John"

#Ex6
x = y = z = "Orange"

#Ex7
def myfunc():

  global x
  x = "fantastic"


#Data type

x = 5
print(type(x))

#ans is integer

x = "Hello World"
print(type(x))

#ans is string

x = 20.5
print(type(x))

#ans is float

x = ["apple", "banana", "cherry"]
print(type(x))

#ans is list

x = ("apple", "banana", "cherry")
print(type(x))

#ans is tuple

x = {"name" : "John", "age" : 36}
print(type(x))

#ans is dict

x = True
print(type(x))

#ans is bool

#Numbers

#Ex1
x = 5
x = float(x)

#Ex2
x = 5.5
x = int(x)

#Ex3
x = 5
x = complex(x)


#Strings
#Ex1
x = "Hello, World"
print(len(x))

#Ex2
txt = "Hello World"
x = txt[0]

#Ex3
txt = "Hello World"
x = txt[2:5]

#Ex4
txt = " Hello World "
x = txt.strip()

#Ex5
txt = "Hello World"
txt = txt.upper()

#Ex6
txt = "Hello World"
txt = txt.lower()

#Ex7
txt = "Hello World"
txt = txt.replace("H", "J")

#Ex8
age = 36
txt = "My name is John, and I am{}"
print(txt.format(age))

#Boolean
#Ex1
print(10 > 9)

# ans is True

#Ex2
print(10 == 9)

# ans is False

#Ex3
print(10 < 9)

#ans is False

#Ex4
print(bool("abc"))

#ans is True

#Ex5
print(bool(0))

#ans is False

#Operators
#Ex1
print(10*5)

#Ex2
print(10/2)

#Ex3
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")


#Ex4
if 5 != 10:
  print("5 and 10 is not equal")

#Ex5
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")


#Lists
#Ex1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#Ex2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#Ex3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#Ex4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")

#Ex5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#Ex6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#Ex7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#Ex8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#Tuples
#Ex1
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#Ex2
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#Ex3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#Ex4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#Sets
#Ex1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#Ex2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#Ex3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#Ex4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#Ex5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#Dictionaries

#Ex1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#Ex2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

#Ex3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

#Ex4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

#Ex5
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#If...Else...
#Ex1
a = 50
b = 10
if
 a > b:
  print("Hello World")

#Ex2
a = 50
b = 10
if
 a != b:
  print("Hello World")

#Ex3
a = 50
b = 10
if
 a == b:
  print("Yes")
else:
  print("No")

#Ex4
a = 50
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")

#Ex5
if a == b and c == d:
  print("Hello")

#Ex6
if a == b or c == d:
  print("Hello")

#Ex7
if 5 > 2:
   print("Five is greater than two!")

#Ex8
if 5 > 2:print("Five is greater than two!")

#Ex9
print("Yes") if 5 > 2 else print("No")


#While loops
#Ex1
i = 1
while i < 6:
  print(i)
  i += 1

#Ex2
i = 1
while i < 6:
  if i == 3:   
    break
  i += 1


#Ex3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


#Ex4
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#For loops

#Ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Ex2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


#Ex3
for x in 
range(6):
  print(x)


#Ex4

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":  
    break
  print(x)


#Functions

#Ex1
def my_function():
  print("Hello from a function")

#Ex2
def my_function():
  print("Hello from a function")

my_function()

#Ex3
def my_function(fname, lname):
  print(fname)

#Ex4
def my_function(x):
  
return x + 5

#Ex5
def my_function(*kids):
  print("The youngest child is " + kids[2])

#Ex6
def my_function(**kid):
  print("His last name is " + kid["lname"])

#Lambda

#Ex1
x = lambda a : a

#Classes

#Ex1

class MyClass:
  x = 5

#Ex2
class MyClass:
  x = 5
p1 = MyClass()

#Ex3
class MyClass:
  x = 5
p1 = MyClass()

print(p1.x)

#Ex4
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age


#Inheritance

#Ex1
class Student(Person):

#Ex2
class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()

#Modules

#Ex1
import mymodule

#Ex2
import mymodule as mx

#Ex3
import mymodule
print(dir(mymodule))

#Ex4
from mymodule import person1














	
