from market import Market
import evaluation
import serialDictatorship
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

    row = [n,m,t,partial,serial_happy,serial_percent_served,serial_avg_time,mod_happy,mod_percent_served,mod_avg_time]
    writer.writerow(row)


results_file = open('results.csv','w+')
results_writer = csv.writer(results_file)
header = ["n","m","t","partial","serial_happy","serial_percent_served","serial_avg_time","mod_happy","mod_percent_served","mod_avg_time"]
results_writer.writerow(header)

n_vals = range(50,1000,50)
m_vals = range(5, 100, 5)
t_vals = range(5, 100, 5)
partial_vals = [False]

for n in n_vals:
    print "------ n: " + str(n)
    for m in m_vals:
        print "m: " + str(m)
        for t in t_vals:
            for partial in partial_vals:
                test_market(n, m, t, partial, results_writer)

results_file.close()
