
# Try out at home before 12.Nov.2026

secret_pin = "4321"
user_entered_pin = input("Enter PIN: ")

while user_entered_pin != secret_pin:
    print("Wrong PIN, try again")
    user_entered_pin = input("Enter PIN: ")

print("Access granted")
