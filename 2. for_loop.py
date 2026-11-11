countOfStudents =  int(input("Enter the number of students in the class : "))

studentName = []
for index in range(countOfStudents):
    name = input(f"Enter the name of Student {index+1} : ")
    studentName.append(name)

studentName.pop()
print(studentName)
for printIndex in range(len(studentName)):
    print(f"Student {printIndex+1} : {studentName[printIndex]}")

#print(studentName[len(studentName)-1])