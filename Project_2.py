class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # Integer between 0 and 100

    # Method to return student grade
    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []  # To hold student details

    # Method to add students to a course
    def add_student(self, student):
        # Test there is room in the class
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True  # To confirm student added
        return False  # Where student not added

    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.get_grade()
            return total/len(course1.students)


# Main routine

# Instantiate 5 student objects
s1 = Student("Timmy", 19, 95)
s2 = Student("Kent", 20, 97)
s3 = Student("Bill", 18, 88)
s4 = Student("Daniel", 18, 76)
s5 = Student("Isla", 19, 3)

# Instantiate course object
course1 = Course("Computer Science", 2)


# Add student to a course
course1.add_student(s1)
course1.add_student(s2)
print(course1.add_student(s3))
print(course1.add_student(s4))

# Get the average grade of all students in a course
print(f"The average grade in {course1.name} is "
      f"{course1.get_average_grade()}")
