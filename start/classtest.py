class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


class Teacher(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student('xujixiao', 121)
student.print_score()
