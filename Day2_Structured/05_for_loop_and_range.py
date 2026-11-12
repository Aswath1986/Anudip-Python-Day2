"""
==========================================================================
 Day 2 | Lesson 05 : for loop and range()
==========================================================================
 What you will learn
   1. Why we need loops
   2. range(start, stop, step)
   3. for loop - repeat a FIXED number of times
   4. Class program: read N student names and print them

 Run this file :  python 05_for_loop_and_range.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. Why loops?
# --------------------------------------------------------------------------
# Without a loop, to read 5 names we would write input() 5 times.
# With 100 students that is impossible. A loop REPEATS a block of code.

# --------------------------------------------------------------------------
# 2. range(start, stop, step)
# --------------------------------------------------------------------------
#   start -> optional, default 0
#   stop  -> MANDATORY, the loop stops BEFORE reaching it
#   step  -> optional, default 1

print(list(range(5)))           # [0, 1, 2, 3, 4]      stop only
print(list(range(1, 6)))        # [1, 2, 3, 4, 5]      start, stop
print(list(range(0, 10, 2)))    # [0, 2, 4, 6, 8]      start, stop, step
print(list(range(5, 0, -1)))    # [5, 4, 3, 2, 1]      counting down

# --------------------------------------------------------------------------
# 3. for loop syntax
# --------------------------------------------------------------------------
#   for variable in range(...):
#       code to repeat        <- must be INDENTED (4 spaces)

for index in range(3):
    print("Loop round number", index)

# --------------------------------------------------------------------------
# 4. Class program - collect and print student names
# --------------------------------------------------------------------------
count_of_students = int(input("Enter the number of students in the class : "))

student_names = []
for index in range(count_of_students):
    # index goes 0, 1, 2 ...  but humans count from 1, so we show index+1
    name = input(f"Enter the name of Student {index + 1} : ")
    student_names.append(name)

print("\nAll students :", student_names)

# Print each student using its index
for print_index in range(len(student_names)):
    print(f"Student {print_index + 1} : {student_names[print_index]}")

# A simpler way: loop directly over the list items
print("\nSame list, looping over items directly:")
for name in student_names:
    print(name)


# ==========================================================================
# PREDICT before you run!
#   for i in range(2, 11, 3):
#       print(i)
#
# TRY IT YOURSELF
#   1. Print the multiplication table of 7 (7 x 1 = 7 ... 7 x 10 = 70).
#   2. In the class program, call student_names.pop() before printing.
#      Whose name disappears? Why?
#   3. Print the student names in REVERSE order using range(..., -1, -1).
# ==========================================================================
