"""
==========================================================================
 Day 2 | Lesson 07 : The uniqueness of while - looping until something happens
==========================================================================
 What you will learn
   1. When to choose for and when to choose while
   2. A loop where we DON'T KNOW how many times it will run
   3. Class program: PIN check

 Run this file :  python 07_while_loop_condition_based.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. for vs while
# --------------------------------------------------------------------------
#   for   -> we KNOW the count in advance  ("read 5 names")
#   while -> we repeat UNTIL a condition changes, count unknown
#            ("keep asking until the PIN is correct")
#
# In Lesson 06 we used while like a for loop (with a counter).
# Here is what makes while UNIQUE: no counter at all.

# --------------------------------------------------------------------------
# 2. Class program - PIN check
# --------------------------------------------------------------------------
# The user may get it right on the 1st try, or the 10th. We cannot know.

secret_pin = "4321"                       # string, because input() gives strings
entered_pin = input("Enter PIN: ")        # ask ONCE before the loop

while entered_pin != secret_pin:          # repeat while it is WRONG
    print("Wrong PIN, try again")
    entered_pin = input("Enter PIN: ")    # ask again -> this is the UPDATE

print("Access granted")

# Notice the pattern:
#   ask once  ->  while wrong:  complain, ask again  ->  success
# input() is written TWICE. Lesson 10 (walrus operator) removes the repeat.


# ==========================================================================
# PREDICT before you run!
#   What happens if secret_pin = 4321 (a number, no quotes)?
#   Will "Access granted" ever print?  Why not?
#
# TRY IT YOURSELF
#   1. Count the attempts and print "Access granted after 3 attempts".
#   2. Keep asking the user for numbers and adding them to a total
#      until they type 0. Then print the total.
# ==========================================================================
