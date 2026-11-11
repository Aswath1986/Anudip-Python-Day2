#Try out in home

correct_pin = "4321"
entered = input("Enter PIN: ")

while entered != correct_pin:
    print("Wrong PIN, try again")
    entered = input("Enter PIN: ")

print("Access granted")