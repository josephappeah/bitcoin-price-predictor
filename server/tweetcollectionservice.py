#====================================================================
# 	author 	: 	joseph appeah
# 	desc  	: 	python tweet collector & analyzer
#====================================================================


# requirements ======================================================
from flask import Flask
from tweetcollector import *
from tweetparser import *
import json
import requests
import random
import os
import os.path
import glob
import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import threading
#====================================================================



# init ==============================================================

#
all_collected_data_as_json 		=	{}


# import the data storage csv file
with open('hourly_sentiment_vals.csv') as hourly_sentiment_vals:

	#
	content 	= hourly_sentiment_vals.readlines()
	content 	= [x.strip() for x in content]
	hr_count  	= 1
	
	#
	for line in content[1:]:
		#
		line_parts 		= line.split(',')
		day_entry  		= {}

		#
		day_entry['date'] 				= 	line_parts[0]
		#day_entry['closing_price'] 	= 	line_parts[1]
		#day_entry['sentiment'] 		= 	line_parts[2]

		#
		for item in line_parts[3:]:
			day_entry[hr_count]   		= line_parts[hr_count]
			hr_count += 1

		#
		hr_count 	= 1

		all_collected_data_as_json[line_parts[0]] = day_entry

		print all_collected_data_as_json

# utils =============================================================

# runs function func periodically
def setInterval(func,time):
    e = threading.Event()
    #
    while not e.wait(time):
    	#
        store_parsed_data(obtain_tweet_sentiment(func()))


def write_stored_json_data_to_file(data):
	#
	with open('sentiments.json', 'w') as outfile:
		json.dump(data, outfile)

#
def store_parsed_data(data):
	#
	hourly_average 	= get_average_sentiment(data)
	today_date 		=  datetime.datetime.now().strftime("%m/%d/%Y")
	hour 			= datetime.datetime.now().hour

	#
	if today_date in all_collected_data_as_json:
		all_collected_data_as_json[today_date][hour] = hourly_average
	else:
		all_collected_data_as_json[today_date] = {}
		all_collected_data_as_json[today_date][hour] = hourly_average
	
	#
	write_stored_json_data_to_file(all_collected_data_as_json)

#====================================================================



# run
setInterval(collect_tweets, 3600) #1 hr