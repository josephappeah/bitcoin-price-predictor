#====================================================================
# 	author 	: 	joseph appeah
# 	desc  	: 	python tweet collector & analyzer
#====================================================================


#	This is a service that runs hourly and collects tweets using the
#	twitter api and then performs sentiment analysis on them. The 
#	sentiment data is stored hourly and averaged out daily.

import sys
sys.path.insert(0, '../utils/')


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
from apscheduler.schedulers.blocking import BlockingScheduler
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
	with open('../storage/hourly_sentiment_vals.csv') as hourly_sentiment_vals:

		#
		file_content 	= hourly_sentiment_vals.readlines()
		file_content 	= [line.strip() for line in file_content]
		hourly_count  	= 1		# needed to iterate through hours in a day
		daily_count 	= 1 	# daily ndx to maintain order of json from dict
		
		
		# parse each line for date, hourly sentiments
		for line in file_content[1:]:
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
def write_stored_json_data_to_file(data):
	'''
		stores json data in memory to dump file 'sentiments.json'
	'''
	with open('../storage/sentiments.json', 'w') as outfile:
		json.dump(data, outfile)


#
def store_as_sample_tweets(data):
	with open('../storage/sample_tweets.txt', 'w') as outfile:
		for item in data:
			line = clean_tweet(item[1]) + "SPLIT-DELIMITER" + str(item[2]) + "\n"
			outfile.write(line)


#
def store_parsed_data(data):
	#
	#store_as_sample_tweets(data)

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

		sentiment_data_json[current_max]['daily_avg']   = round(float(daily_sum)/float(hour),3)
	else:
		sentiment_data_json[current_max]				= {}
		sentiment_data_json[current_max]['date']		= today_date 		
		sentiment_data_json[current_max][hour] 			= hourly_average
		sentiment_data_json[current_max]['daily_avg'] 	= hourly_average

	#
	write_stored_json_data_to_file(sentiment_data_json)


#
def service():
	store_parsed_data(obtain_tweet_sentiment(collect_tweets()))
#====================================================================



# run
create_sentiment_json_dump()

#
scheduler = BlockingScheduler()
scheduler.add_job(service, 'interval', hours=1)
scheduler.start()