#Try out in home before 12.Nov.2026

secret_pin = "4321"
entered_num = input("Enter PIN: ")

while entered_num != secret_pin:
    print("Wrong PIN, try again")
    entered_num = input("Enter PIN: ")

print("Access granted")