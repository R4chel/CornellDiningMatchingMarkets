from market import Market
import evaluation
import serialDictatorship
import minLocations
import csv


def test_market(n, m, t, partial, writer):
    market = Market(n, m, t, partial)
    serialDictatorship.serial_dictatorship(market)
    serial_happy = evaluation.happy(market)
    serial_percent_served = evaluation.percent_served(market)
    serial_avg_time = evaluation.average_time(market)

    market.reset()
    serialDictatorship.modified_serial_dictatorship(market)
    mod_happy = evaluation.happy(market)
    mod_percent_served = evaluation.percent_served(market)
    mod_avg_time = evaluation.average_time(market)

    market.reset()
    minLocations.minimize_locations(market)
    min_loc_happy = evaluation.happy(market)
    min_loc_percent_served = evaluation.percent_served(market)
    min_loc_avg_time = evaluation.average_time(market)

    row = [n, m, t, partial, serial_happy, serial_percent_served,
           serial_avg_time, mod_happy, mod_percent_served, mod_avg_time,
           min_loc_happy, min_loc_percent_served, min_loc_avg_time]
    writer.writerow(row)


results_file = open('results.csv', 'w+')
results_writer = csv.writer(results_file)
header = ["n", "m", "t", "partial", "serial_happy", "serial_percent_served",
          "serial_avg_time", "mod_happy", "mod_percent_served", "mod_avg_time",
          "min_loc_happy", "min_loc_percent_served", "min_loc_avg_time"]
results_writer.writerow(header)

n_vals = range(100, 1000, 100)
m_vals = range(10, 100, 10)
t_vals = range(10, 100, 10)
partial_vals = [False, True]

for partial in partial_vals:
    for t in t_vals:
        for n in n_vals:
            for m in m_vals:
                print("Testing partial={0} t={1} n={2} m={3}".format(partial,
                                                                     t, n, m))
                test_market(n, m, t, partial, results_writer)

results_file.close()
