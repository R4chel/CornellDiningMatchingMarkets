from market import Market

def serial_dictatorship(market):
    for student in market.students:
        for location_index in student.pref_list:
            if market.locations[location_index].serve_student(student):
                break

def modified_serial_dictatorship(market):
    max_students_served = sum([location.max_students() for location in market.locations])
    min_unserved = len(market.students) - max_students_served
    n = 0
    unserved_students = [student for student in market.students if student.location is None]
    while len(unserved_students) > min_unserved and n < len(market.locations) - 1:
        unserved_students = [student for student in unserved_students if not market.locations[student.pref_list[n]].serve_student(student)]
        n += 1


