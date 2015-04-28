import random


class DiningLocation:

    def __init__(self, index):
        self.index = index
        self.base_time = random.choice(range(10, 30))
        self.num_students = 0

    def serve_student(self, s):
        self.num_students += 1
        s.location = self

    def serving_time(self):
        return self.base_time + self.num_students

    def max_students(self, max_time):
        return max_time - self.base_time

    def full(self, max_time):
        return self.max_students(max_time) >= self.num_students


class Student:

    def __init__(self, index, locations, incomplete_prefs):
        self.index = index
        self.pref_list = random.shuffle(locations)
        self.location = None
        if incomplete_prefs:
            list_size = random.uniform(1, len(locations))
            self.pref_list = self.pref_list[0:list_size]

    def happiness(self, m):
        if self.location is None:
            return 0
        if self.location not in self.pref_list:
            return -1
        location_index = self.pref_list.index(self.location)
        return float(m - location_index) / m

m = 10
n = 100
locations = [DiningLocation(i) for i in range(m)]
students = [Student(i, locations, False) for i in range(n)]
