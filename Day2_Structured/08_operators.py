"""
==========================================================================
 Day 2 | Lesson 08 : Operators
==========================================================================
 What you will learn
   1. Arithmetic operators   +  -  *  /  //  %  **
   2. Relational operators   ==  !=  >  <  >=  <=     (answer is True/False)
   3. Assignment operators   =  +=  -=  *=  /=  //=
   4. (Preview - Day 3) Logical operators  and  or  not

 Run this file :  python 08_operators.py
==========================================================================
"""

a = 17
b = 5

# --------------------------------------------------------------------------
# 1. Arithmetic operators
# --------------------------------------------------------------------------
print("a + b  =", a + b)      # 22   addition
print("a - b  =", a - b)      # 12   subtraction
print("a * b  =", a * b)      # 85   multiplication
print("a / b  =", a / b)      # 3.4  division -> ALWAYS a float
print("a // b =", a // b)     # 3    floor division -> drops the decimal part
print("a % b  =", a % b)      # 2    remainder (modulus)
print("a ** 2 =", a ** 2)     # 289  power

# --------------------------------------------------------------------------
# 2. Relational (comparison) operators -> result is True or False
# --------------------------------------------------------------------------
print("a == b :", a == b)     # False  equal to   (TWO = signs!)
print("a != b :", a != b)     # True   not equal to
print("a > b  :", a > b)      # True
print("a < b  :", a < b)      # False
print("a >= 17:", a >= 17)    # True
print("a <= 16:", a <= 16)    # False

# Strings can be compared too
print("SAVE10" == "SAVE10")   # True
print("save10" == "SAVE10")   # False -> comparison is case sensitive

# We can store the True/False result in a variable
is_adult = a >= 18
print("is_adult :", is_adult)

# --------------------------------------------------------------------------
# 3. Assignment operators - shortcuts to update a variable
# --------------------------------------------------------------------------
#   x += 5   means   x = x + 5
score = 10
score += 5
print("after += 5 :", score)     # 15
score -= 3
print("after -= 3 :", score)     # 12
score *= 2
print("after *= 2 :", score)     # 24
score /= 5
print("after /= 5 :", score)     # 4.8   (became a float)
score //= 1
print("after //= 1:", score)     # 4.0   (decimal removed)

# --------------------------------------------------------------------------
# 4. PREVIEW (Day 3) - Logical operators combine True/False values
# --------------------------------------------------------------------------
#   and -> True only if BOTH sides are True
#   or  -> True if AT LEAST ONE side is True
#   not -> flips True <-> False
print(True and False, True or False, not True)   # False True False


# ==========================================================================
# PREDICT before you run!
#   print(10 / 2)      print(10 // 3)      print(10 % 3)      print(2 ** 10)
#   x = 7;  x += x;  print(x)
#
# TRY IT YOURSELF
#   1. Ask for a number and print True if it is even (hint: % 2 == 0).
#   2. Convert 135 minutes into hours and minutes using // and %.
# ==========================================================================
