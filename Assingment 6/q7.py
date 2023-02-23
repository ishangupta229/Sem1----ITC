class Student:
    pass

class Marks:
    pass

student1 = Student()
marks1 = Marks()

print(+(student1, Student))
print(isinstance(marks1, Marks))
print(issubclass(Student, object))
print(issubclass(Marks, object))
