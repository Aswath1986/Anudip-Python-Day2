
# Try out at home before 12.Nov.2026

secret_pin = "4321"
# user_entered_pin = input("Enter PIN: ")

# while user_entered_pin != secret_pin:

while (user_entered_pin := input("Enter PIN: ")) != secret_pin:
    # Both assignment of input to user_entered_pin and return the value to larger expression
    print("Wrong PIN, try again")
    user_entered_pin = input("Enter PIN: ")

print("Access granted")
