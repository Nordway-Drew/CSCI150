# Well commented code is essential to any project

"This line will be skipped by the interpreter"

"""
The triple quotation mark syntax starts a multi-line string
   They will preserve both indentation and line spacing
This is standard syntax for multi-line comments in Python

"""

#########
# PRINT #
#########

print("Hello World")

print(["Hello", "World"])
print(42)
# Will not work.
# print ("Hello World" + 42)
x = 42
print("Hello World ", x)

##################
# Dynamic Typing #
##################

# Python has no keyword for declaring a variable
x = "Hello World"
# A variable can be redeclared any time
x = 42

# Multiple variables can be declared in one line
x, y, z = "car", "bike", "unicycle"
# naming convention is underscores between words
my_programming_language = "Python"

############################
# Variables and Data Types #
############################

# Numbers

# int: Whole numbers, positive or negative, of arbitrary length
x = 10
# float: Positive or negative number containing one or more decimals
y = 3.14
# complex: Numbers with an imaginary component, denoted with a j
z = 3j

# use variables to redeclare its self
x = x + 10
print("x = x + 10 :", x)

#########
# INPUT #
#########

# Execution will be paused until input is provided
print("Enter your name")
name = input()
print("name is of class ", type(name))

# A string can be passed to the input function
# That string will be printed ON the input line
age = input("Enter your age: ")
print("age is of class ", type(name))

# Input is read as a String
print("Hello " + name + ", you are " + age + " years old")

print("How old will I be in 30 years?")
answer = int(age) + 30
print("you will be ", answer)
# or
print("you will be ", (int(age) + 30))
# or
age = int(input("Enter your age: "))
print("age is of class ", type(age))
