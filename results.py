from market import Market
import evaluation
import serialDictatorship

market = Market(150, 10, 45, False)
serialDictatorship.modified_serial_dictatorship(market)
evaluation.happy(market)
evaluation.percent_served(market)
evaluation.average_time(market)
market.reset_market()
serialDictatorship.serial_dictatorship(market)
evaluation.happy(market)
evaluation.percent_served(market)
evaluation.average_time(market)

