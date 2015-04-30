import random


class DiningLocation:

    def __init__(self, index, max_time):
        self.index = index
        self.base_time = random.choice(range(10, 30))
        self.num_students = 0
        self.max_time = max_time

    def serve_student(self, s):
        if not self.full():
            self.num_students += 1
            s.location = self
            return True
        else:
            return False

    def serving_time(self):
        return self.base_time + self.num_students

    def max_students(self):
        return self.max_time - self.base_time

    def full(self):
        return self.num_students >= self.max_students()


class Student:

    def __init__(self, index, locations, incomplete_prefs):
        self.index = index

        # Make duplicates of locations, first location in locations list
        # appears 1 time, last location appears m times
        multiple_locations = []
        for location in locations:
            for i in range(location.index + 1):
                multiple_locations.append(location.index)

        self.pref_list = []
        while len(multiple_locations) > 0:
            loc = random.choice(multiple_locations)
            self.pref_list.append(loc)
            while loc in multiple_locations:
                multiple_locations.remove(loc)

        self.location = None

        if incomplete_prefs:
            list_size = random.choice(range(1, len(locations)))
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
        self.students = [Student(i,
                                 self.locations,
                                 incomplete_prefs) for i in range(n)]
        self.max_time = max_time
m = 10
n = 100
max_time = 45
market = Market(n, m, max_time)
