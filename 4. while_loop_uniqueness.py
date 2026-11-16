#Try out in home before 12.Nov.2026

secret_pin = "0515"
entered_num = input("Enter PIN: ")

while entered_num != secret_pin:
    print("Invalid PIN, try again")
    entered_num = input("Enter PIN: ")

print("Access granted")

# output:
# Enter PIN: 0515
# Access granted
