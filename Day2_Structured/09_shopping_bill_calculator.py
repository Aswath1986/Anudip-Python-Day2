"""
==========================================================================
 Day 2 | Lesson 09 : Mini Project - Shopping Bill Calculator
==========================================================================
 This program uses EVERYTHING from Lesson 08 together.
 Work through it with the PRIMM method we practised on 11.Nov.2026:

   P - PREDICT     : read the code, write down what each print will show
   R - RUN         : run it and compare with your prediction
   I - INVESTIGATE : change one value at a time - what changes?
   M - MODIFY      : take input from the user instead of fixed values
   M - MAKE        : build your own bill calculator (see bottom)

 Run this file :  python 09_shopping_bill_calculator.py
==========================================================================
"""

# --------------------------------------------------------------------------
# Step 1 - Inputs
# --------------------------------------------------------------------------
item_price = 450
quantity = 3
is_member = True
coupon_code = "SAVE10"

# --------------------------------------------------------------------------
# Step 2 - ARITHMETIC operators: compute the bill
# --------------------------------------------------------------------------
subtotal = item_price * quantity        # 450 * 3        = 1350
tax = subtotal * 18 / 100               # 18% of 1350    = 243.0
bill = subtotal + tax                   # 1350 + 243.0   = 1593.0

print("Subtotal            :", subtotal)
print("Tax (18%)           :", tax)
print("Bill before discount:", bill)

# --------------------------------------------------------------------------
# Step 3 - RELATIONAL operators: check the rules (True / False)
# --------------------------------------------------------------------------
big_order = subtotal >= 1000            # True  -> 1350 is at least 1000
has_coupon = coupon_code == "SAVE10"    # True  -> code matches exactly

print("Big order           :", big_order)
print("Has coupon          :", has_coupon)

# Day 3 preview - LOGICAL operators will combine these rules:
#   gets_discount = (big_order and is_member) or has_coupon
#   free_shipping = big_order and not (quantity > 10)

# --------------------------------------------------------------------------
# Step 4 - ASSIGNMENT operators: update the bill in place
# --------------------------------------------------------------------------
gets_discount = has_coupon              # for Day 2 we use only the coupon rule

if gets_discount:                       # 'if' runs the next line only when True
    bill *= 0.9                         # 10% off  ->  bill = bill * 0.9  = 1433.7

bill //= 1                              # drop the paise  ->  1433.0
bill += 0                               # no change - shows += works on floats too

print("Final bill          :", bill)


# ==========================================================================
# INVESTIGATE
#   a) Change quantity to 2. Is it still a big order?
#   b) Change coupon_code to "save10". What is the final bill now? Why?
#   c) Remove the line  bill //= 1 . What does the final bill look like?
#
# MODIFY
#   Replace the fixed inputs with input(), e.g.
#       item_price = int(input("Enter item price : "))
#
# MAKE
#   Build a "Restaurant Bill": number of people, cost per plate,
#   5% GST, and a 15% tip. Print every step like this program does.
# ==========================================================================
