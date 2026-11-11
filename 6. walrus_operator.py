#Try out in home before 12.Nov.2026

secret_pin = "4321"
#entered_num = input("Enter PIN: ")

#while entered_num != secret_pin:

while (entered_num := input("Enter PIN: ")) != secret_pin:  
#both assignment of input to entered_num and return the value to larger expression
    print("Wrong PIN, try again")
    entered_num = input("Enter PIN: ")

print("Access granted")