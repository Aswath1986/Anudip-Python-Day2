
# Day 2 Lab — Program 2: Shopping Bill Calculator

# --- Inputs ---
product_price = 450
item_quantity = 3
member_status = True
discount_coupon = "SAVE10"

# --- Arithmetic: compute the bill ---
base_amount = product_price * item_quantity       # 1350
tax_amount = base_amount * 18 / 100                # 243.0
total_bill = base_amount + tax_amount              # 1593.0

print("Subtotal:", base_amount)
print("Tax (18%):", tax_amount)
print("Bill before discount:", total_bill)

# --- Relational + Logical: eligibility rules ---
is_large_order = base_amount >= 1000
coupon_available = discount_coupon == "SAVE10"

print("Big order:", is_large_order)                 # True


# --- Assignment: apply the discount in place ---
discount_eligible = 1  # only for Day 2 practice

if discount_eligible:
    total_bill *= 0.9      # 10% off → total_bill = total_bill * 0.9

total_bill //= 1           # floor to whole rupees/dollars
total_bill += 0            # no-op, shows += works on floats too

print("Final bill:", total_bill)
