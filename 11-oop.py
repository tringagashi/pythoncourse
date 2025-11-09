class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, I am {self.name} and I am {self.age} years old.")

s = Student("Tringa", 22)
s.introduce()
