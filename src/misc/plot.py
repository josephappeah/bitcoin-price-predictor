
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.patches as mpatches
import datetime as dt

dates = []
btc = []
sent = []

with open('../server/storage/sents.txt','r') as sample_tweets:
	#
	file_content 	= sample_tweets.readlines()
	file_content 	= [line.strip() for line in file_content]

	# parse each line for date, hourly sentiments

	for line in file_content[1:]:
		line_parts = line.split(",")
		dates.append(line_parts[0])
		btc.append(float(line_parts[1]))
		sent.append(float(line_parts[2]))



x = [dt.datetime.strptime(d,'%m/%d/%y').date() for d in dates]

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

plt.gcf().autofmt_xdate()


fig, ax1 = plt.subplots()

ax1.plot(x, btc, 'b-', label='BTC/USD Closing Prices')
ax1.set_xlabel('Dates')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('BTC/USD Daily Closing Prices', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(x,sent, 'r-', label='Tweet Sentiment')
ax2.set_ylabel('Daily Twitter Sentiment Values', color='r')
ax2.tick_params('y', colors='r')

ax1.legend(loc=0)
ax2.legend(loc=3)

#fig.tight_layout()
plt.gcf().autofmt_xdate()
plt.savefig("Test")
