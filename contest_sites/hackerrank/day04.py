#!/usr/bin/python3

class Person:
    def __init__(self, initialAge):
        if initialAge < 0:
            print('Age is not valid, setting age to 0.')
            self.age = 0
        else:
            self.age = initialAge


    def amIOld(self):
        if self.age < 13:
            print('You are young.')
        elif self.age >= 13 and self.age < 18:
            print('You are a teenager.')
        else:
            print('You are old.')


for i in range(0,20):
    p = Person(i)
    print(i)
    p.amIOld()
