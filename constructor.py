class Student:
    name = "chiranjith"
    # constructor
    def __init__(self, fullname):
        self.name = fullname
        print("creating new student for database")

s1 = Student("karan")
print(s1.name)  #karan

    