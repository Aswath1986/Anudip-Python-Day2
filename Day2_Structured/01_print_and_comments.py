"""
==========================================================================
 Day 2 | Lesson 01 : print() and Comments
==========================================================================
 What you will learn
   1. How to show output on the screen using print()
   2. How to print many values at once
   3. What comments are and why we use them

 Run this file :  python 01_print_and_comments.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. Your first program
# --------------------------------------------------------------------------
# print() shows whatever is inside the brackets on the screen.
# Text must be written inside quotes  "..."  or  '...'  -> this is a STRING.

print("This is my first program")
print('Hello World')            # single quotes work exactly the same way


# --------------------------------------------------------------------------
# 2. Printing many values at once
# --------------------------------------------------------------------------
# Separate values with a comma. print() puts ONE SPACE between them.

print("Python", "is", "fun")            # Python is fun
print("5 + 5 =", 5 + 5)                 # 5 + 5 = 10   (Python does the maths)

# sep  -> what to put BETWEEN values   (default is a space " ")
# end  -> what to put at the END       (default is a new line "\n")
print("11", "11", "2026", sep="-")      # 11-11-2026
print("Same line ->", end=" ")
print("continued here")


# --------------------------------------------------------------------------
# 3. Comments
# --------------------------------------------------------------------------
# A line starting with  #  is a COMMENT. Python ignores it completely.
# We use comments to:
#   a) explain our code to other people (and to our future self)
#   b) temporarily "switch off" a line without deleting it

# print("This line will NOT run because it is commented out")

print("Comments can also come after code")   # <- this part is ignored

"""
Text inside triple quotes that is not stored anywhere behaves like a
multi-line comment. It is mostly used to describe a file or a function
(like the box at the top of this file).
"""


# ==========================================================================
# PREDICT before you run!
#   What will each line print?
#       print("A", "B", "C", sep="")
#       print("Day", 2, end="!\n")
#
# TRY IT YOURSELF
#   1. Print your name, your city and your college on ONE line,
#      separated by " | ".
#   2. Comment out the very first print() in this file and run again.
# ==========================================================================
