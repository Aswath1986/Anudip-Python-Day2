"""
==========================================================================
 Day 2 | Lesson 10 : The Walrus Operator  :=
==========================================================================
 What you will learn
   1. What := does (assign AND use a value in one step)
   2. How it removes the repeated input() from the PIN program
   3. A common mistake to avoid

 Needs Python 3.8 or newer.
 Run this file :  python 10_walrus_operator.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. What is :=  ?   (it looks like the eyes and tusks of a walrus)
# --------------------------------------------------------------------------
#   =    stores a value.                 It is a STATEMENT.
#   :=   stores a value AND gives it     It is an EXPRESSION, so it can be
#        back to the bigger expression.  used INSIDE a condition.

print(total := 10 + 5)      # stores 15 in total AND prints 15
print(total)                # 15

# --------------------------------------------------------------------------
# 2. PIN program - before and after
# --------------------------------------------------------------------------
# BEFORE (Lesson 07): input() is written twice
#
#   entered_pin = input("Enter PIN: ")
#   while entered_pin != secret_pin:
#       print("Wrong PIN, try again")
#       entered_pin = input("Enter PIN: ")
#
# AFTER: input() is written once, inside the condition

secret_pin = "4321"

while (entered_pin := input("Enter PIN: ")) != secret_pin:
    # Each round:
    #   1. input() reads the PIN
    #   2. := stores it in entered_pin
    #   3. the same value is compared with secret_pin
    print("Wrong PIN, try again")

print("Access granted. You entered", entered_pin)

# --------------------------------------------------------------------------
# 3. Common mistakes
# --------------------------------------------------------------------------
# a) Asking AGAIN inside the loop body:
#        while (entered_pin := input("Enter PIN: ")) != secret_pin:
#            print("Wrong PIN, try again")
#            entered_pin = input("Enter PIN: ")    # <- WRONG!
#    The condition already asks for input. This extra line asks a second
#    time, and that answer is thrown away without being checked.
#
# b) Forgetting the brackets:
#        while entered_pin := input("Enter PIN: ") != secret_pin:
#    Python does the != FIRST, so entered_pin becomes True/False, not the PIN.


# ==========================================================================
# PREDICT before you run!
#   print((x := 4) * x)
#
# TRY IT YOURSELF
#   Rewrite Lesson 07's "add numbers until 0" exercise using :=
#       while (num := int(input("Number (0 to stop): "))) != 0:
#           ...
# ==========================================================================
