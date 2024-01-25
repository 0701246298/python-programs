class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def display_info(self):
        print(f"Name: {self.fname} {self.lname}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, fname, lname, age, regno, department, hostel, meanscore):
        super().__init__(fname, lname, age)
        self.regno = regno
        self.department = department
        self.hostel = hostel
        self.meanscore = meanscore

    def display_info(self):
        super().display_info()
        print(f"Registration Number: {self.regno}")
        print(f"Department: {self.department}")
        print(f"Hostel: {self.hostel}")
        print(f"Mean Score: {self.meanscore}")


# Create an instance of the Student class
student = Student("Maureen", "Musungu", 21, "12345", "Computer Science", "MaryLand", 85.5)

# Display student information
student.display_info()
