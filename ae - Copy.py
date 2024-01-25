class Employee:
    def message(self):
        print("this is message class")


class Company(Employee):
    def message(self):
        print("This is company class")

emp = Employee()
emp.message()
Comp = Company()
Comp.message()
