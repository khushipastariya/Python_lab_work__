# Python_lab_work__
class Person(object):
    # Constructor
def __init__(self, name):
        self.name = name
defgetName(self):
        return self.name
defisEmployee(self):
        return False

# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

    # Here we return true
defisEmployee(self):
        return True
if __name__=='__main__':
emp = Person("Naruto") # An Object of Person
    print(emp.getName(), emp.isEmployee())

emp = Employee("Kakashi") # An Object of 
    print(emp.getName(), emp.isEmployee())
