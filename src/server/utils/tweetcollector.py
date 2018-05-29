#==================================================================================
# author 	: joseph appeah
# date  	: 05/01/2018
# desc  	: python tweet collector
#==================================================================================


# This is a wrapper for the TwitterSearch python library for the purposed of the 
# project. It has all params for collecting tweets about bitcoin based on filters 
# specified for the project.


# requirements ====================================================================
import TwitterSearch
import json
import os.path
import datetime
#==================================================================================


# essentials ======================================================================

# load twitter api configs from local config file
with open('../configs.json') as configs_file:    
    configs = json.load(configs_file)

# keywords for twitter search
keywords = ['BTC',
			'BITCOIN',
			'#BTC',
			'#BITCOIN',
			'CRYPTO', 
			'#CRYPTO', 
			'#CRYPTOTRADING',
			'CRYPTOTRADING'
		]

#==================================================================================




# utils ===========================================================================

#
def parse_datetime_to_parts(datetime):
	'''
		parses date time from the twitter api into parts
	'''
	#
	datetime_parts 	= []
	
	#
	[date, time] 	= 	datetime.split(" ")

	#
	datetime_parts.extend(date.split("-"))
	datetime_parts.extend(time.split(":")[:2])
	datetime_parts.extend(time.split(":")[2].split("."))

	#
	return datetime_parts


# collects all tweets
def collect_tweets():
	'''
		collects the tweets from twitter. only gets the last 500 which
		is the maximum allowed by the api.
	'''
	# 
	tweets 						= []

	#
	try:

		#
	    tso 					= TwitterSearch.TwitterSearchOrder()
	    tso.set_keywords(keywords) 
	    tso.set_language('en')
	    tso.set_include_entities(False)
	    tso.set_count(100)

	    #
	    ts = TwitterSearch.TwitterSearch (
	        consumer_key 		= configs['consumer_key'],
	        consumer_secret 	= configs['consumer_secret'],
	        access_token 		= configs['access_token'],
	        access_token_secret = configs['access_token_secret']
	     )

	    #
	    for tweet in ts.search_tweets_iterable(tso):
	    	tweets.append((tweet['created_at'], tweet['text']))

	except TwitterSearch.TwitterSearchException as e:
		print e
		None

	#
	return tweets

#==================================================================================




