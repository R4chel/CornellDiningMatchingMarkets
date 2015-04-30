def minimize_locations(market):
    locations_max_served = [location.max_students()
                            for location in market.locations]
    _, sorted_locations = zip(*sorted(zip(locations_max_served,
                                          market.locations)))
    sorted_locations = list(sorted_locations)
    sorted_locations.reverse()

    num_locations = len(sorted_locations)
    for location in sorted_locations:
        for i in range(num_locations):
            for student in market.students:
                if(not location.full() and student.location is None
                   and len(student.pref_list) > i
                   and student.pref_list[i] == location.index):
                    location.serve_student(student)
