"""
==========================================================================
 Day 2 | Lesson 04 : Lists - storing many values in one variable
==========================================================================
 Why this lesson comes before loops:
   In the loop programs we collect many student names. We need a LIST
   to hold them. So let us understand lists first.

 What you will learn
   1. Creating a list
   2. Indexing  - getting one item (index starts at 0!)
   3. len()     - how many items
   4. append()  - add an item at the end
   5. pop()     - remove the last item

 Run this file :  python 04_lists_basics.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. Creating a list
# --------------------------------------------------------------------------
student_names = []                          # an empty list
fruits = ["apple", "banana", "mango"]       # a list with 3 items
print(student_names)
print(fruits)

# --------------------------------------------------------------------------
# 2. Indexing - positions start at 0
# --------------------------------------------------------------------------
#      "apple"   "banana"   "mango"
#  index  0         1          2
#  neg   -3        -2         -1

print(fruits[0])        # apple   (first)
print(fruits[2])        # mango
print(fruits[-1])       # mango   (-1 always means LAST)

# --------------------------------------------------------------------------
# 3. len() - number of items
# --------------------------------------------------------------------------
print(len(fruits))                  # 3
print(fruits[len(fruits) - 1])      # mango -> last index is ALWAYS len - 1

# --------------------------------------------------------------------------
# 4. append() - add to the end
# --------------------------------------------------------------------------
student_names.append("Ravi")
student_names.append("Priya")
student_names.append("Karthik")
print(student_names)                # ['Ravi', 'Priya', 'Karthik']

# --------------------------------------------------------------------------
# 5. pop() - remove (and return) the last item
# --------------------------------------------------------------------------
removed = student_names.pop()
print("Removed :", removed)         # Karthik
print(student_names)                # ['Ravi', 'Priya']


# ==========================================================================
# PREDICT before you run!
#   nums = [10, 20, 30, 40]
#   print(nums[1], nums[-2], len(nums))
#   print(nums[4])        # what happens here? (hint: IndexError)
#
# TRY IT YOURSELF
#   1. Make a list of 4 cities. Print the first and last using indexes.
#   2. Append one more city, pop it back out, and print the list.
# ==========================================================================
