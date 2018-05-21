#========================================================================
# author 					: joseph appeah
# desc 						: 
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

#
server 			= Flask(__name__)
server_port 	= 3000

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

#
@server.route("/get-sentiments")
def get_sentiments():
	#
	return json.dumps(import_sentiments())


#
@server.route("/get-btc-status")
def get_btc_status():
	#
	return json.dumps({"price" : 500, "sentiment" : 0.56, "prediction" : True})

#
@server.route("/get-sentiment-graph-data")
def get_sentiment_graph_data():
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
server.run(port=server_port)
