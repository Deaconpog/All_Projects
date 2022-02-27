class AllStaff: # This is the main class that covers all attributes
    def __init__(self, name, age, emp_id, birth_date, job_title):
        self.name = name
        self.age = age
        self.emp_id = emp_id
        self.birth_date = birth_date
        self.job_title = job_title

    def show(self):
        print(f"{self.emp_id} is {self.name} aged {self.age} being born"
              f"{self.birth_date} employed as {self.job_title}")


# Child classes contain attributes unique to that class
class Management(AllStaff):
    def __init__(self, name, age, emp_id, birthdate, job_title, car): # Adds a car attribute unique to management
        super().__init__(self, name, age, emp_id, birthdate, job_title) # Gets name and age attributes from class (AllStaff)
        self.car = car

    def show(self):
        print(f"{self.emp_id} is {self.name} aged {self.age} being born "
              f"{self.birthdate} employed as {self.job_title} and drives a "
              f"{self.car}")

class Clerical(AllStaff):
