"""
==========================================================================
 Day 2 | Lesson 03 : Number Systems and Characters
==========================================================================
 What you will learn
   1. Decimal, Binary, Octal and Hexadecimal numbers
   2. bin(), oct(), hex()  - convert decimal to other systems
   3. int(text, base)      - convert back to decimal
   4. ord() and chr()      - characters and their number codes (ASCII)

 Run this file :  python 03_number_systems_and_characters.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. Number systems
# --------------------------------------------------------------------------
#   System        Base   Digits used             Python prefix
#   Decimal        10    0-9                     (none)
#   Binary          2    0 1                     0b
#   Octal           8    0-7                     0o
#   Hexadecimal    16    0-9 and A-F             0x
#
# Computers store everything in BINARY (0s and 1s).

# --------------------------------------------------------------------------
# 2. Decimal  ->  other systems
# --------------------------------------------------------------------------
print(bin(5))       # 0b101   ->  4 + 0 + 1 = 5
print(oct(8))       # 0o10    ->  1*8 + 0   = 8
print(hex(10))      # 0xa     ->  a means 10
print(hex(255))     # 0xff    ->  15*16 + 15 = 255

# --------------------------------------------------------------------------
# 3. Other systems  ->  decimal
# --------------------------------------------------------------------------
print(int("101", 2))     # 5
print(int("ff", 16))     # 255
print(0b101, 0xff)       # Python understands the prefixes directly: 5 255

# --------------------------------------------------------------------------
# 4. Characters and ASCII codes
# --------------------------------------------------------------------------
# Every character has a number code.
#   ord(character) -> number      chr(number) -> character

print(ord('C'), " ", ord('F'))     # 67   70
print(chr(122), chr(91))           # z [

print(ord('A'), ord('a'))          # 65 97  -> capital and small differ by 32
print(chr(ord('a') - 32))          # A      -> small letter to capital!


# ==========================================================================
# PREDICT before you run!
#   print(bin(8))          print(chr(66))          print(ord('0'))
#
# TRY IT YOURSELF
#   1. Ask the user for a number (use int(input(...))) and print it in
#      binary, octal and hexadecimal.
#   2. Ask the user for a single letter and print its ASCII code.
#   3. Print the letters A to E using chr() and the numbers 65 to 69.
# ==========================================================================
