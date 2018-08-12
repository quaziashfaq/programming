#!/usr/bin/python3

def gcd(a, b):
    r = b % a
    while r != 0:
        b = a
        a = r
        r = b % a
    return a

def gcd_array(numbers):
    '''Provide an array of numbers. Array size must be > 1. Return value is gcd of all numbers'''
    if len(numbers) == 1:
        print('numbers array size = 1')
        return
    else:
        g = numbers[0]
        for i in range(1, len(numbers)):
            g = gcd(g, numbers[i])
    return g


def lcm(numbers):
    '''Provide an array of numbers. Array size must be > 1. Return value is lcm of all numbers'''
    if len(numbers) == 1:
        print('numbers array size = 1')
        return
    else:
        g = gcd_array(numbers)
        numbers = [i/g for i in numbers]
        m = 1
        for i in numbers:
            m = m * i
        return int(g * m)


class Student:
    def __init__(self, student_id, awake_time, sleep_time, position):
        self.student_id = student_id
        self.sleep_time = sleep_time
        self.awake_time = awake_time
        self.state = 0
        self.state_pos = 0
        self.starting_state = position

        if self.starting_state <= self.awake_time:
            #self.state = 0 # I am awake
            self.state = 'awake'
            self.state_pos = self.awake_time - self.starting_state
        else:
            #self.state = 1 # I am sleeping
            self.state = 'sleeping'
            self.state_pos = self.sleep_time - (self.starting_state - self.awake_time)
        return

    def getState(self):
        return self.state, self.state_pos

    def nextState(self, awake_no, sleeping_no):
        if self.state == 'sleeping':
            if self.state_pos > 0:
                self.state_pos -= 1
            elif self.state_pos == 0:
                self.state = 'awake'
                self.state_pos = self.awake_time - 1
            else:
                print('I should not be printed!!')
        elif self.state == 'awake':
            if self.state_pos > 0:
                self.state_pos -= 1
            elif self.state_pos == 0:
                if sleeping_no > awake_no:
                    self.state = 'sleeping'
                    self.state_pos = self.sleep_time - 1
                else:
                    self.state = 'awake'
                    self.state_pos = self.awake_time - 1
            else:
                print('I should not be printed!!')
        else:
            print('I should not be printed!!')
        return


class SleepingClass:
    def __init__(self, n):
        '''students is an array Student class'''
        self.sleeping = 0
        self.awake = 0
        self.n = n
        self.students = []
        return

    def getStudentState(self, student_id, awake_time, sleep_time, position):
        self.students.append(Student(student_id, awake_time, sleep_time, position))

    def calculateClassState(self):
        self.awake = 0
        self.sleeping = 0
        for s in self.students:
            # print(s.state)
            if s.state == 'awake':
                self.awake += 1
            elif s.state == 'sleeping':
                self.sleeping += 1
            else:
                print("1. I should not be printed!!")

        if self.n != self.awake + self.sleeping:
            print("Logic Error: Number of students don't match")
        return

    def nextTick(self):
        self.calculateClassState()
        for s in self.students:
            s.nextState(self.awake, self.sleeping)
        return


'''
s1 = Student(2, 4, 1)
s2 = Student(1, 5, 2)
s3 = Student(1, 4, 3)

print(s1.getstate())
print(s2.getstate())
print(s3.getstate())
'''

n = int(input())
caseno = 1
found = False
while n!= 0:
    c = SleepingClass(n)
    for i in range(n):
        line = [int(j) for j in input().strip().split()]
        c.getStudentState(i, line[0], line[1], line[2])

    t = [(s.awake_time + s.sleep_time) for s in c.students]
    l = lcm(t)

    #for s in c.students:
    #    print(s.getState())

    c.calculateClassState()
    for i in range(2*l):
        #print('pass no: {}'.format(i))
        if c.sleeping == 0:
            found = True
            break
        else:
            c.nextTick()
    if found == True:
        print('Case {}: {}'.format(caseno, i))
    elif found == False:
        print('Case {}: {}'.format(caseno, -1))

    # next input
    n = int(input())
    caseno += 1
    found = False
