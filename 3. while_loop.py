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