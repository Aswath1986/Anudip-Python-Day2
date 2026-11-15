
number_of_students = int(input("Enter the number of students : "))  # 5
student_index = 0
student_names = []

# range(start - 0 default, stop - mandatory, increment - optional (default =1))
while(student_index <= number_of_students-1):  # start <= stop
    student_name = input(f"Enter the name of student {student_index} : ")
    student_names.append(student_name)
    student_index = student_index + 1

print_index = 0
remaining_count = len(student_names)

while(remaining_count > 0):
    print(f"Enter the name of student {print_index} : ", student_names[print_index])
    print_index = print_index + 1
    remaining_count = remaining_count - 1
