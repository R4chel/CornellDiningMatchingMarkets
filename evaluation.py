def happy(market):
    m = len(market.locations)
    happy = [student.happiness(m) for student in market.students]
    return sum(happy)


def percent_served(market):
    num_served = sum([1 for student in market.students
                      if student.location is not None])
    return float(num_served) / len(market.students)


def total_time(market):
    serving_time = [student.location.serving_time() for student
                    in market.students if student.location is not None]
    return sum(serving_time)


def average_time(market):
    num_served = sum([1 for student in market.students
                      if student.location is not None])
    if num_served == 0:
        return 0
    return float(total_time(market)) / num_served
