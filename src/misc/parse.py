'''
with open('moving_avg.csv') as hourly_sentiment_vals:

	#
	content 	= hourly_sentiment_vals.readlines()
	content 	= [line.strip() for line in content]
	date 	   	= []
	returns 	= []
	strategy_5 	= []
	strategy_10 = []
	strategy_15 = []
	strategy_20 = []
	
	
	# parse each line for date, hourly sentiments
	for line in content[1:]:
		line_parts 	= line.split(",")


		date.append(line_parts[0])
		returns.append(round(float(line_parts[1]),3))
		strategy_5.append(round(float(line_parts[2]),3))
		strategy_10.append(round(float(line_parts[3]),3))
		strategy_15.append(round(float(line_parts[4]),3))
		strategy_20.append(round(float(line_parts[5]),3))


	print "dates"
	print date
	print "\n"

	print "returns"
	print returns
	print "\n"

	print "strategy_5"
	print strategy_5
	print "\n"

	print "strategy_10"
	print strategy_10
	print "\n"

	print "strategy_15"
	print strategy_15
	print "\n"

	print "strategy_20"
	print strategy_20
	print "\n"
'''

with open('out.csv') as hourly_sentiment_vals:

	#
	content 	= hourly_sentiment_vals.readlines()
	content 	= [line.strip() for line in content]
	date 	   	= []
	actual_price	= []
	predicted_price 	= []

	
	
	# parse each line for date, hourly sentiments
	for line in content:
		line_parts 	= line.split(",")
		date.append(line_parts[0])
		actual_price.append(round(float(line_parts[1]),3))
		predicted_price.append(round(float(line_parts[2]),3))

	print "dates"
	print date
	print "\n"

	print "returns"
	print actual_price
	print "\n"

	print "strategy_5"
	print predicted_price 
	print "\n"
