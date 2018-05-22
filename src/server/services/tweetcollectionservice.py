#====================================================================
# 	author 	: 	joseph appeah
# 	desc  	: 	python tweet collector & analyzer
#====================================================================


#	This is a service that runs hourly and collects tweets using the
#	twitter api and then performs sentiment analysis on them. The 
#	sentiment data is stored hourly and averaged out daily.


# requirements ======================================================
import json
import threading
import requests
import random
import os
import os.path
import glob
import datetime

from flask import Flask
from tweetcollector import *
from tweetparser import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#====================================================================




# global vars =======================================================
sentiment_data_json 	=	{}
#====================================================================



# utils =============================================================

#
def create_sentiment_json_dump():

	'''
		creates a json dump from the 'hourly_sentiment_csv' file.
		this file has the data collected with TwitterArchiver
		module
	'''

	#
	with open('hourly_sentiment_vals.csv') as hourly_sentiment_vals:

		#
		file_content 	= hourly_sentiment_vals.readlines()
		file_content 	= [line.strip() for line in file_content]
		hourly_count  	= 1		# needed to iterate through hours in a day
		daily_count 	= 1 	# daily ndx to maintain order of json from dict
		
		
		# parse each line for date, hourly sentiments
		for line in content[1:]:
			#
			line_parts 	= line.split(',')
			day_entry  	= {}

			#
			day_entry['date'] 		= line_parts[0]
			day_entry['daily_avg'] 	= line_parts[2]

			#
			for item in line_parts[3:]:
				day_entry[hourly_count]		= line_parts[hourly_count]
				hourly_count				+= 1

			#
			hourly_count = 1

			#
			sentiment_data_json[daily_count] = day_entry
			daily_count 					+= 1

	
	#
	sentiment_data_json['max'] 	= daily_count # store the max val for future data addition
	daily_count 				= 1


#
def setInterval(func, time):
	'''
		runs the function 'func' every 'time' seconds
	'''
    e = threading.Event()
    #
    while not e.wait(time):
    	#
        store_parsed_data(obtain_tweet_sentiment(func()))


#
def write_stored_json_data_to_file(data):
	'''
		stores json data in memory to dump file 'sentiments.json'
	'''
	with open('sentiments.json', 'w') as outfile:
		json.dump(data, outfile)


#
def store_parsed_data(data):
	#
	hourly_average 	= get_average_sentiment_from_tweets(data)
	today_date 		= datetime.datetime.now().strftime("%m/%d/%Y")
	hour 			= datetime.datetime.now().hour
	current_max 	= sentiment_data_json['max']

	#
	if current_max in sentiment_data_json:
		sentiment_data_json[current_max][hour] 			= hourly_average

		# update daily average
		daily_sum 	= 0
		for hr in range(1,hour):
			daily_sum += sentiment_data_json[current_max][hr]

		sentiment_data_json[current_max]['daily_avg']   = round(float(daily_sum)/float(hour),2)
	else:
		sentiment_data_json[current_max]				= {}
		sentiment_data_json[current_max]['date']		= today_date 		
		sentiment_data_json[current_max][hour] 			= hourly_average
		sentiment_data_json[current_max]['daily_avg'] 	= hourly_average

	#
	write_stored_json_data_to_file(sentiment_data_json)

#====================================================================



# run

create_sentiment_json_dump() 
setInterval(collect_tweets, 3600) #1 hr