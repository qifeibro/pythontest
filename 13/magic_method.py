"""
Python - Magic or Dunder Methods
Magic methods in Python are the special methods that start and end with the double underscores. 
They are also called dunder methods. Magic methods are not meant to be invoked directly by you, 
but the invocation happens internally from the class on a certain action. For example, 
when you add two numbers using the + operator, internally, the __add__() method will be called.

Built-in classes in Python define many magic methods. 
Use the dir() function to see the number of magic methods inherited by a class.
"""

class Student:
    """
    A class representing a student.

    Attributes:
    -----------
    name : str
        The name of the student.
    age : int
        The age of the student.

    Methods:
    --------
    __eq__(__o)
        Returns True if this student has the same age as the other student, False otherwise.
    """

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __eq__(self, __o: object) -> bool:
        return self.age == __o.age

stu1 = Student("周杰轮", 11)
stu2 = Student("林军杰", 11)
print(stu1 != stu2) # False
print(stu1 == stu2) # True
print(dir(int)) # lists all the attributes and methods defined in the int class
