# Day 2 Lab — Program 2: Shopping Bill Calculator
# LEARN and implement below using PRIMM method which we tried on 11.November.2026
# PREDICT, REFLECT, INVESTIGATE, MODIFY, MAKE 
# Show what has been tried in tomorrow's class

# --- Inputs ---
item_price = 450
quantity = 3
is_member = True
coupon_code = "SAVE10"

# --- Arithmetic: compute the bill ---
subtotal = item_price * quantity            # 1350
tax = subtotal * 18 / 100                   # 243.0
bill = subtotal + tax                       # 1593.0
print("Subtotal:", subtotal)
print("Tax (18%):", tax)
print("Bill before discount:", bill)

# --- Relational + Logical: eligibility rules ---
big_order = subtotal >= 1000
has_coupon = coupon_code == "SAVE10"
#We will cover in Day 3 - gets_discount = (big_order and is_member) or has_coupon
#We will cover in Day 3 - free_shipping = big_order and not (quantity > 10)

print("Big order:", big_order)              # True
#We will cover in Day 3 - print("Gets discount:", gets_discount)      # True
#We will cover in Day 3 - print("Free shipping:", free_shipping)      # True

# --- Assignment: apply the discount in place ---
gets_discount = 1 #only for Day 2 practice
if gets_discount:
    bill *= 0.9      # 10% off  → bill = bill * 0.9
bill //= 1           # floor to whole rupees/dollars
bill += 0            # no-op, shows += works on floats too

print("Final bill:", bill)      