print("Maximum students is 20")
studentList = []
gradeList = []


def mainloop():
    maxstudentList = 20
    while len(studentList) < maxstudentList:
        student = input("Enter student name: ")
        if not student.isalpha():
            print("Please enter valid characters in students name")
        else:

            grades = int(input("Enter students grade: "))
            if grades >= 0 and grades <= 100:
                studentList.append(student)
                gradeList.append(grades)

                print("Current students: ", studentList)
                print("Grades of students:", gradeList)
            else:
                print("Not a correct grade")


mainloop()


def average():
    total = sum(gradeList)
    length = len(gradeList)
    averages = total / length
    print("The average grade: ", averages)


average()
