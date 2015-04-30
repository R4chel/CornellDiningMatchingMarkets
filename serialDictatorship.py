from market import Market


def serial_dictatorship(market):
    for student in market.students:
        for location_index in student.pref_list:
            if market.locations[location_index].serve_student(student):
                break

market = Market(100, 10, 35, False)
serial_dictatorship(market)

max_students = [loc.max_students() for loc in market.locations]
print max_students
print sum(max_students)

happy = [student.happiness(10) for student in market.students]
print happy
print sum(happy)
