countOfStudents =  int(input("Enter the number of students in the class : "))

studentName = []
for index in range(countOfStudents):
    name = input(f"Enter the name of Student {index+1} : ")
    studentName.append(name)

studentName.pop()
print(studentName)
lengthofstudentName=len(studentName)
for printIndex in range(lengthofstudentName):
    print(f"Student {printIndex+1} : {studentName[printIndex]}")

#print(studentName[len(studentName)-1])
# output:
# Enter the number of students in the class : 4
# Enter the name of Student 1 : Yash
# Enter the name of Student 2 : res
# Enter the name of Student 3 : niki
# Enter the name of Student 4 : sherin
# ['Yash', 'res', 'niki']
# Student 1 : Yash
# Student 2 : res
# Student 3 : niki
