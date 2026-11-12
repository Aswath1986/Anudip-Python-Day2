"""
==========================================================================
 Day 2 | Lesson 02 : Variables, input() and f-strings
==========================================================================
 What you will learn
   1. Variables  - giving a NAME to a value
   2. input()    - reading a value typed by the user
   3. Escape characters  \"  \n  \t
   4. f-strings  - the easiest way to mix text and values
   5. id()       - where a value lives in memory

 Run this file :  python 02_variables_input_fstrings.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. Variables
# --------------------------------------------------------------------------
# A variable is a name that points to a value.   name = value
# The  =  sign means "store the right side into the left side".

my_name = "Aswath"          # a string (text)
age = 25                    # an int (whole number)
height = 5.9                # a float (decimal number)

print(my_name, age, height)
print(type(my_name), type(age), type(height))   # type() tells the data type


# --------------------------------------------------------------------------
# 2. Reading input from the user
# --------------------------------------------------------------------------
# input("message") shows the message, waits for the user to type,
# and gives back what was typed.
# IMPORTANT: input() ALWAYS returns a STRING, even if the user types 25.

my_name = input("Enter the name of the user : ")
print("Hello", my_name)


# --------------------------------------------------------------------------
# 3. Escape characters
# --------------------------------------------------------------------------
# Some characters cannot be typed directly inside a string.
# We put a backslash  \  in front of them:
#     \"   a double quote inside a "..." string
#     \n   new line
#     \t   tab space

print("Hello \"" + my_name + "\"")      # Hello "Aswath"
print("Line one\nLine two")
print("Name\tAge")


# --------------------------------------------------------------------------
# 4. f-strings  (formatted strings)
# --------------------------------------------------------------------------
# Put the letter  f  before the quotes. Anything inside { } is evaluated
# by Python and its value is placed in the text.

print(f"Hello \"{my_name}\",\n your lucky number is {5 * 5}")

# Compare the three ways of printing the same sentence:
print("Hello", my_name, "you are", age)              # commas
print("Hello " + my_name + " you are " + str(age))   # + joins strings only
print(f"Hello {my_name} you are {age}")              # f-string (cleanest)


# --------------------------------------------------------------------------
# 5. id() - the memory address of a value
# --------------------------------------------------------------------------
# Every value is stored somewhere in memory. id() gives that location
# as a number. Two variables with the same id point to the SAME object.

address_identity = id(my_name)
print(f"Address of the user's saved location : {address_identity}")

copy_name = my_name
print(id(copy_name) == id(my_name))     # True -> both names point to one value


# ==========================================================================
# PREDICT before you run!
#   num = input("Enter a number: ")      # user types 5
#   print(num + num)                     # 10 or 55 ?  Why?
#
# TRY IT YOURSELF
#   1. Ask the user for their name and city and print:
#         Welcome "Ravi" from Chennai!
#      using an f-string.
#   2. Ask for a number, convert it with int(), and print its square.
# ==========================================================================
