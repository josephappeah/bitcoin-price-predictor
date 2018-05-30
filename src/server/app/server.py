#========================================================================
# author 					: joseph appeah
# desc 						: backend server for btc price predictor
#========================================================================


import sys
sys.path.insert(0, '../utils/')

# requirements ======================================================
from flask import Flask
import json
import requests
import random
import os
import os.path
import glob
import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from flask_cors import CORS
from tweetcollector import *
from tweetparser import *

#
app 			= Flask(__name__)
server_port 	= 3000
CORS(app)

#========================================================================

def import_sentiments():
	#
	with open('../storage/sentiments.json','r') as sentiments_file:    
		sentiments = json.load(sentiments_file)
	#
	return sentiments

#========================================================================
# endpoints
#========================================================================


@app.route("/get-sample-tweets")
def get_sample_tweets():
	#
	result = {}

	#
	with open('../storage/sample_tweets.txt','r') as sample_tweets:
		#
		file_content 	= sample_tweets.readlines()
		file_content 	= [line.strip() for line in file_content]
		tw_count 		= 1
		
		# parse each line for date, hourly sentiments
		for line in file_content:
			entry      = {}
			line_parts = line.split("SPLIT-DELIMITER")
			tweet 	   = line_parts[0]
			rating     = line_parts[1]

			entry['tweet'] 		= tweet
			entry['rating']  	= round(float(rating),3)
			result[tw_count] 	= entry
			tw_count += 1

	#
	return json.dumps(result)


#
@app.route("/get-sentiments")
def get_sentiments():
	#
	return json.dumps(import_sentiments())

#
@app.route("/get-nextday-predictions")
def get_nextday_prediction():
	#
	price 	= round(float(open('../modules/next_day/ensemble_NEXTDAY.txt','r').readline().rstrip()),2)
	return str(price)

#
@app.route("/get-todays-predictions")
def get_startup_utils():
	#
	try:
		current_sentiment 	= float(get_average_sentiment_from_tweets(obtain_tweet_sentiment(collect_tweets())))
	except:
		current_sentiment  	= 0.5

	#
	price 				= round(float(open('../modules/next_day/ensemble_NEXTDAY.txt','r').readline().rstrip()),2)
	
	#
	return json.dumps({"price" : price, "sentiment" : current_sentiment, "prediction" : True})


#
@app.route("/retrain-modules")
def retrain_ml_modules():
	#
	return 'retraining ML modules'

#
@app.route("/get-current-sentiment-value")
def get_current_sentiment_val():
	#
	current_sentiment = float(get_average_sentiment_from_tweets(obtain_tweet_sentiment(collect_tweets())))
	#
	return json.dumps({"current_sentiment" : current_sentiment})

#
@app.route("/get-sentiment-data")
def get_sentiment_data():
	#
	sentiments 	= import_sentiments()
	result 		= {}
	labels 		= []
	sentiment  	= []
	btc_price 	= []

	#
	for key in sentiments:
		labels.append(sentiments[key]['date'])
		btc_price.append(float(sentiments[key]['closing_price']))
		sentiment.append(float(sentiments[key]['sentiment']))

	#
	result['labels'] 		= labels
	result['sentiments'] 	= sentiment
	result['btc_price'] 	= btc_price

	#
	return json.dumps(result)

#

if __name__ == 'main':
	app.run(port=server_port)

#app.run(port=server_port)