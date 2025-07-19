class Student:
    def __init__(self,name):
        self.__name = name
    def display(self):
        print(f'student name in class = {self.__name}')

s1=Student('Rama')
s1.display()
s1.__name = 'Krishna'
print(f'stundet name otuside class - {s1.__name}')
s1.display()
print('bug fix on hot fix by vinay')

print("Enhancement2 Z9XX00A2")

print('enhancement1 z8xx00a1')

