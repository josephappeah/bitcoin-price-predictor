from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from math import sqrt
from numpy import *
from pandas import *
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot
import data
import os
import sys
import quandl
quandl.ApiConfig.api_key = 'qinG5wphqPidgvqrpbPW'

EPOCHS = 250


if(len(sys.argv) !=4):
	SAMPLE_SIZE = 395
	VALIDATION_DAYS = 20
	TEST_DAYS = 30 + 1
else:
	SAMPLE_SIZE = int(sys.argv[1])
	VALIDATION_DAYS = int(sys.argv[2])
	TEST_DAYS = int(sys.argv[3]) + 1

#BATCH_SIZE = 1
BATCH_SIZE = SAMPLE_SIZE - (TEST_DAYS + VALIDATION_DAYS)

'''
features = ["BCHAIN/MKPRU","BCHAIN/MWNUS", "BCHAIN/CPTRV","BCHAIN/BLCHS", "BCHARTS/KRAKENEUR", "BCHAIN/NTRBL",
    "BCHAIN/ETRAV", "BCHAIN/MKTCP", "BCHAIN/TRFUS", "BCHAIN/TRVOU", "BITFINEX/LTCBTC",
    "BCHAIN/HRATE", "BCHARTS/BITSTAMPUSD","BCHAIN/DIFF","BCHAIN/MIREV","BCHAIN/ATRCT","BCHAIN/CPTRA","BCHAIN/NTREP","BCHAIN/NADDU","BCHAIN/TOTBC]"

'''

features = ["BCHAIN/MKPRU","BCHAIN/MWNTD", "BCHAIN/AVBLS", "BCHARTS/KRAKENEUR", "BCHAIN/NTRBL",
    "BCHAIN/ETRAV", "BCHAIN/MKTCP", "BCHAIN/TRFUS",
    "BCHAIN/HRATE", "BCHARTS/BITSTAMPUSD","BCHAIN/DIFF","BCHAIN/MIREV","BCHAIN/ATRCT","BCHAIN/CPTRA","BCHAIN/NTREP","BCHAIN/NADDU","BCHAIN/TOTBC"]
    
drop = range(len(features)+1, (len(features)+1)*2 -2)


def createFeaturesCSV(m, csvname):

	try:
    		os.remove(csvname)
			#print('Removing old copy of %s' %csvname)
	except OSError:
    		pass

	n = len(features)
	X = np.zeros([n+1,m])
	headers = "DAY, "
	for i, s in enumerate(features):
		if(i != len(features)-1):
			headers += s + ", "
		else:
			headers += s

	X[0,:] = range(1,m+1)

	for i, feature in enumerate(features):
		print('Fetching: %s from Quandl' %feature)
		_, X[i+1, :] = data.get_data(feature, SAMPLE_SIZE)	
	np.fliplr(X)
	print('')
	np.savetxt(csvname, X.transpose(), fmt='%.8f', delimiter=',', header= headers)
	
# convert series to supervised learning: pushes column for variable to predict by 1
# (since we are using t to predict t+1)
def format_output_column(data, n_in=1, n_out=1, dropnan=True):
	n_vars = 1 if type(data) is list else data.shape[1]
	df = DataFrame(data)
	cols, names = list(), list()
	# input sequence (t-n, ... t-1)
	for i in range(n_in, 0, -1):
		cols.append(df.shift(i))
		names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
	# forecast sequence (t, t+1, ... t+n)
	for i in range(0, n_out):
		cols.append(df.shift(-i))
		if i == 0:
			names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
		else:
			names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
	# put it all together
	agg = concat(cols, axis=1)
	agg.columns = names
	# drop rows with NaN values
	if dropnan:
		agg.dropna(inplace=True)
	return agg


# load dataset
csv_file = "Features.csv"
createFeaturesCSV(SAMPLE_SIZE, csv_file)
#createFeaturesCSV(1, "todayFeature.csv")
dataset = read_csv(csv_file, header=0, index_col=0)
#print(dataset)
values = dataset.values

# convert data to float
values = values.astype('float64')


#normalize features using MinMax between 0 and 1
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)
# frame as supervised learning
reframed = format_output_column(scaled, 1, 1)
# drop columns we don't want to predict
reframed.drop(reframed.columns[drop], axis=1, inplace=True)
# split into train and test sets
values = reframed.values

# leave last VALIDATION_DAYS days for testing
n_train_hours = SAMPLE_SIZE - VALIDATION_DAYS - TEST_DAYS
train = values[:n_train_hours, :]
test = values[n_train_hours:n_train_hours + VALIDATION_DAYS, :]
test_real = values[n_train_hours + VALIDATION_DAYS:, :]
test_1day = values[n_train_hours + VALIDATION_DAYS + TEST_DAYS:, :]
# split into input and outputs
train_X, train_y = train[:, :-1], train[:, -1]
test_X, test_y = test[:, :-1], test[:, -1]
testR_X, testR_y = test_real[:, :-1], test_real[:, -1]
test_1day_X =  test_real[:, :-1]

'''
print('Test Prices')
print(testR_y)
'''

# reshape input to be 3D [samples, timesteps, features]F
train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
testR_X = testR_X.reshape((testR_X.shape[0], 1, testR_X.shape[1]))

 
# design network
model = Sequential()
model.add(LSTM(400, return_sequences=True,input_shape=(train_X.shape[1], train_X.shape[2])))
model.add(Dense(1))
#model.add(LSTM(200), return_sequences=True)
model.add(LSTM(400, return_sequences=False))

model.add(Dense(1))
model.compile(loss='mae', optimizer='adam')

# fit network
history = model.fit(train_X, train_y, epochs=EPOCHS, batch_size=BATCH_SIZE, validation_data=(test_X, test_y), verbose=2, shuffle=True)
# plot history
pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='validate')
pyplot.legend()
pyplot.title('LSTM Fitting')
pyplot.xlabel('Epochs', fontsize=16)
pyplot.ylabel('Value Loss', fontsize=16)
pyplot.savefig("LSTM_valueLoss_Training.png")
#pyplot.show()

# make a prediction on the test data
yhat = model.predict(test_X)
test_X = test_X.reshape((test_X.shape[0], test_X.shape[2]))
# invert scaling for forecast
inv_yhat = concatenate((yhat, test_X[:, 1:]), axis=1)
inv_yhat = scaler.inverse_transform(inv_yhat)
inv_yhat = inv_yhat[:,0]
 

# invert scaling for actual
test_y = test_y.reshape((len(test_y), 1))
inv_y = concatenate((test_y, test_X[:, 1:]), axis=1)
inv_y = scaler.inverse_transform(inv_y)
inv_y = inv_y[:,0]

# Plot Validation Results
pyplot.figure(2)
pyplot.plot(inv_y, marker='o', linestyle='-', color='b', label='Actual Price')
pyplot.plot(inv_yhat, marker='o', linestyle='-', color='r' , label='Forecasted Price using LSTM')
pyplot.legend()
pyplot.title("Testing on the " + str(VALIDATION_DAYS) + "Validation days")
pyplot.xlabel('Days', fontsize=18)
pyplot.ylabel('Bitcoin Price ($)', fontsize=16)
pyplot.savefig("LSTM_Validate.png")
rmse = sqrt(mean_squared_error(inv_y, inv_yhat))
print('\n#########################')
print('Validation Test RMSE: $%.3f' % rmse)

actual_rise = []
predict_rise =[]
for i in range(inv_y.shape[0]-1):
	if(inv_y[i] - inv_y[i+1] < 0):
		actual_rise.append(True)
	else:
		actual_rise.append(False)

	if(inv_y[i] - inv_yhat[i+1] < 0):
		predict_rise.append(True)
	else:
		predict_rise.append(False)

correct_direction_predictCntr = 0

for i, item in enumerate(actual_rise):
	if(item == predict_rise[i]):
		correct_direction_predictCntr +=1

percentage_correct = float(float(correct_direction_predictCntr)/float(len(actual_rise)))*100
print('Detected correct price movement direction in %d/%d (%.2f%%) Test cases\n'
	%(correct_direction_predictCntr, len(actual_rise), percentage_correct))
print('#########################')

####################################################################################################

##    TEST RESULTS

####################################################################################################



yhat = model.predict(testR_X)
testR_X = testR_X.reshape((testR_X.shape[0], testR_X.shape[2]))
# invert scaling for forecast
inv_yhat = concatenate((yhat, testR_X[:, 1:]), axis=1)
inv_yhat = scaler.inverse_transform(inv_yhat)
inv_yhat = inv_yhat[:,0]
 

# invert scaling for actual
testR_y = testR_y.reshape((len(testR_y), 1))
inv_y = concatenate((testR_y, testR_X[:, 1:]), axis=1)
inv_y = scaler.inverse_transform(inv_y)
inv_y = inv_y[:,0]

# Plot Test Results
pyplot.figure(3)
pyplot.plot(inv_y, marker='o', linestyle='-', color='b', label='Actual Price')
pyplot.plot(inv_yhat, marker='o', linestyle='-', color='r' , label='Forecasted Price using LSTM RNN')
pyplot.legend()
pyplot.title("Testing over past " + str(TEST_DAYS-1) + " days")
pyplot.xlabel('Days', fontsize=18)
pyplot.ylabel('Bitcoin Price ($)', fontsize=16)
pyplot.savefig("LSTM_test.png")

if((inv_y.shape[0] != 0)):
	rmse = sqrt(mean_squared_error(inv_y, inv_yhat))
	print('Test RMSE: $%.3f' % rmse)

	actual_rise = []
	predict_rise =[]
	for i in range(inv_y.shape[0]-1):
		if(inv_y[i] - inv_y[i+1] < 0):
			actual_rise.append(True)
		else:
			actual_rise.append(False)

		if(inv_y[i] - inv_yhat[i+1] < 0):
			predict_rise.append(True)
		else:
			predict_rise.append(False)

	correct_direction_predictCntr = 0

	for i, item in enumerate(actual_rise):
		if(item == predict_rise[i]):
			correct_direction_predictCntr +=1

	percentage_correct = float(float(correct_direction_predictCntr)/float(len(actual_rise)))*100
	print('Detected correct price movement direction in %d/%d (%.2f%%) Test cases'
		%(correct_direction_predictCntr, len(actual_rise), percentage_correct))
	print('#########################\n')

	try:
		os.remove('lstm_backtest.csv')
		print('Removing old copy of lstm_backset file..')
	except OSError:
    		pass

	
	dates = data.get_data(features[0],TEST_DAYS-1)[0]
	#dates = (dates[:-1])
	print('Writing to new copy of lstm_backtest file..')
	output = np.array([])
	for i in range(len(dates)):
		val = dates[i] + "," + str(inv_y[i]) + "," + str(inv_yhat[i])
		output = np.append(output,val)
	np.savetxt('lstm_backtest.csv', output,delimiter=',',fmt='%s')

try:
	os.remove('lstm_nextday.csv')
	print('Removing old copy of lstm_nextday file..')
except OSError:
	pass

np.savetxt('lstm_nextday.csv', inv_yhat[-1:])
print('Writing to new copy of lstm_nextday file..')