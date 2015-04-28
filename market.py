import random

class DiningLocation:
    base_time_range = range(10,30)
    def __init__(self, index):
        self.index = index
        self.base_time = random.choice(base_time_range)
        self.num_students = 0

    def serve_student(s):
        self.num_students += 1

    def serving_time():
        return self.base_time + self.num_students

    def max_students(max_time):
        return max_time - self.base_time

    def full(max_time):
        return max_students(max_time) >= self.num_students

class Student:
    __init__(self, index, locations):
        self.index = index
        self.pref_list = random.shuffle(locations)

locations = [ DiningLocation(i) for i in range(m)]
students = [Student(i, locations) for i in range(n)]
