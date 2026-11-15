countOfStudents = int(input("Enter the number of students : ")) #5
index = 0
studentName = [] 

# range(start - 0 default, stop - mandatory, increment - optional (default =1))
while(index <= countOfStudents-1): # start <= stop
    name = input(f"Enter the name of student {index} : ")
    studentName.append(name)
    index  = index + 1

prtIndex = 0
count = len(studentName)
while(count > 0):
    print(f"Enter the name of student {prtIndex} : ", studentName[prtIndex])
    prtIndex  = prtIndex + 1
    count = count - 1

# output:
# Enter the number of students : 5
# Enter the name of student 0 : Yash
# Enter the name of student 1 : resma
# Enter the name of student 2 : sherin
# Enter the name of student 3 : ruffia
# Enter the name of student 4 : priya
#  student 1 :  Yash
#  student 2 :  resma
#  student 3 :  sherin
#  student 4 :  ruffia
#  student 5 :  priya
