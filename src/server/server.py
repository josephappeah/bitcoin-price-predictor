#========================================================================
# author 					: joseph appeah
# desc 						: backend server for btc price predictor
#========================================================================

#========================================================================
# to - do 
#========================================================================
'''
- set up sample tweet server
- set up sentiment provider
- find sentiment json creation
'''
#========================================================================


#
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

#
app 			= Flask(__name__)
server_port 	= 3000
CORS(app)

#========================================================================

def import_sentiments():
	#
	with open('sentiments.json','r') as sentiments_file:    
		sentiments = json.load(sentiments_file)
	#
	return sentiments

#========================================================================
# endpoints
#========================================================================


@app.route("/get-sample-tweets")
def get_sample_tweets():
	return "sample tweets"


#
@app.route("/get-sentiments")
def get_sentiments():
	#
	return json.dumps(import_sentiments())


#
#@app.route("/get-startup-utils")
@app.route("/get-btc-status")
def get_startup_utils():
	#
	return json.dumps({"price" : 500, "sentiment" : 0.56, "prediction" : True})

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
