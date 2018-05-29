#========================================================================
# author 					: joseph appeah
# get sentiment analysis 	: python file that returns realtime analysis
#========================================================================

#
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


#
analyzer 		= 	SentimentIntensityAnalyzer()


# clean up a tweet : remove any unparsable chars
def clean_tweet(tweet):
	new_tweet = ''

	if tweet.find('RT') == -1 and tweet.find('#RT') == -1 and tweet.find('retweet') == -1:
		try:
			new_tweet = tweet.encode('utf-16', errors='ignore')
			new_tweet = tweet.replace('?', '')
			new_tweet = new_tweet.replace(',', '.')
			new_tweet = new_tweet.replace('\u2026', '')
		except Exception as e:
			None
	else:
		None

	return new_tweet


# normalize the sentiment value recieved to 1
def normalize_compound_score_to_one(score):
	#
	return (score + 1)/2


# get the sentiment value 
def get_sentiment_value(tweet):
	#
	return analyzer.polarity_scores(tweet)


# clean up the csv archive
def obtain_tweet_sentiment(data):
	data_with_sentiments = []
	#
	for item in data:
		#
		tweet 	= clean_tweet(item[1])

		#
		if tweet:
			#
			compound_sentiment_val 	= get_sentiment_value(tweet)['compound']
			normalized_value		= normalize_compound_score_to_one(compound_sentiment_val)
			#
			data_with_sentiments.append((item[0], tweet, normalized_value))


	return data_with_sentiments


def get_average_sentiment_from_tweets(data):
	#
	sent_vals 	= []

	#
	for item in data:
		sent_vals.append(float(item[2]))

	#
	try:
		avg = round(float(sum(sent_vals))/float(len(sent_vals)),3)
	except:
		avg = 0.000
	return avg

