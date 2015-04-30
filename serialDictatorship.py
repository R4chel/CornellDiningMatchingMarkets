def serial_dictatorship(market):
    for student in market.students:
        for location_index in student.pref_list:
            if not market.locations[location_index].full():
                market.locations[location_index].serve_student(student)
                break


def modified_serial_dictatorship(market):
    max_students_served = sum([location.max_students()
                              for location in market.locations])
    min_unserved = max(0, len(market.students) - max_students_served)
    n = 0
    unserved_students = list(market.students)

    while (len(unserved_students) > min_unserved
           and n < len(market.locations) - 1):
        still_unserved = []
        for student in unserved_students:
            if n >= len(student.pref_list):
                continue

            next_location = market.locations[student.pref_list[n]]
            if next_location.full():
                still_unserved.append(student)
            else:
                next_location.serve_student(student)
        unserved_students = still_unserved
        n += 1
