"""
==========================================================================
 Day 2 | Lesson 06 : while loop (counter based)
==========================================================================
 What you will learn
   1. while loop syntax
   2. The 3 parts of a counting loop: START, CONDITION, UPDATE
   3. The same student-names program, written with while
   4. Infinite loops and how to avoid them

 Run this file :  python 06_while_loop_counter.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. Syntax
# --------------------------------------------------------------------------
#   while condition:
#       code to repeat
#
# The block keeps running AS LONG AS the condition is True.

# --------------------------------------------------------------------------
# 2. The 3 parts of a counting loop
# --------------------------------------------------------------------------
#   for index in range(0, 3, 1)     is the same as:
#
#   index = 0             <- START      (range start)
#   while index < 3:      <- CONDITION  (range stop)
#       ...
#       index = index + 1 <- UPDATE     (range step)

index = 0
while index < 3:
    print("while round", index)
    index = index + 1

# --------------------------------------------------------------------------
# 3. Class program - student names with while
# --------------------------------------------------------------------------
count_of_students = int(input("Enter the number of students : "))

student_names = []
index = 0                                   # START
while index <= count_of_students - 1:       # CONDITION  (same as index < count)
    name = input(f"Enter the name of student {index + 1} : ")
    student_names.append(name)
    index = index + 1                       # UPDATE

# Printing: this time we count DOWN how many are left to print
print_index = 0
remaining = len(student_names)
while remaining > 0:
    print(f"Student {print_index + 1} : {student_names[print_index]}")
    print_index = print_index + 1
    remaining = remaining - 1

# --------------------------------------------------------------------------
# 4. Infinite loop warning
# --------------------------------------------------------------------------
# If you FORGET the UPDATE line, the condition never becomes False
# and the loop runs forever.  (Press Ctrl + C to stop it.)
#
#   index = 0
#   while index < 3:
#       print(index)          # index is always 0 -> never stops!


# ==========================================================================
# PREDICT before you run!
#   n = 10
#   while n > 0:
#       print(n)
#       n = n - 3
#
# TRY IT YOURSELF
#   1. Print numbers 1 to 10 using while.
#   2. Find the sum of numbers from 1 to 100 using while.
#   3. Rewrite your for-loop multiplication table from Lesson 05 using while.
# ==========================================================================
