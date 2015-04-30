import random


class DiningLocation:

    def __init__(self, index, max_time):
        self.index = index
        self.base_time = random.choice(range(10, 30))
        self.num_students = 0
        self.max_time = max_time

    def serve_student(self, s):
        self.num_students += 1
        s.location = self

    def serving_time(self):
        return self.base_time + self.num_students

    def max_students(self):
        return self.max_time - self.base_time

    def full(self):
        return self.num_students >= self.max_students()


class Student:

    def __init__(self, index, weighted_locations, incomplete_prefs):
        self.index = index

        self.pref_list = []
        weighted_locations = list(weighted_locations)
        while len(weighted_locations) > 0:
            loc = random.choice(weighted_locations)
            self.pref_list.append(loc)
            while loc in weighted_locations:
                weighted_locations.remove(loc)

        self.location = None

        if incomplete_prefs:
            list_size = random.choice(range(1, len(self.pref_list)))
            self.pref_list = self.pref_list[0:list_size]

    def happiness(self, m):
        if self.location is None:
            return 0
        if self.location.index not in self.pref_list:
            return -1
        location_index = self.pref_list.index(self.location.index)
        return float(m - location_index) / m


class Market:
    def __init__(self, n, m, max_time, incomplete_prefs=False):
        self.locations = [DiningLocation(i, max_time) for i in range(m)]

        # Make duplicates of locations, first location in locations list
        # appears 1 time, last location appears m times
        weighted_locations = []
        for location in self.locations:
            for i in range(location.index + 1):
                weighted_locations.append(location.index)

        self.students = [Student(i,
                                 weighted_locations,
                                 incomplete_prefs) for i in range(n)]

        self.max_time = max_time

    def reset(self):
        for location in self.locations:
            location.num_students = 0
        for student in self.students:
            student.location = None

    def students_served(self):
        return sum([1 for student in self.students
                    if student.location is not None])
