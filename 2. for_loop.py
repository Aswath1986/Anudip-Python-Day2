
number_of_students = int(input("Enter the number of students in the class : "))

student_names = []

for student_index in range(number_of_students):
    student_name = input(f"Enter the name of Student {student_index+1} : ")
    student_names.append(student_name)

student_names.pop()
print(student_names)

for print_index in range(len(student_names)):
    print(f"Student {print_index+1} : {student_names[print_index]}")

# print(student_names[len(student_names)-1])
