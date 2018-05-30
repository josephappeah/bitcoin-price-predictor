LSTM README
Author: Agastya Sinha
========================================================================

HOW TO RUN
========================================================================

1) With no command line arguments:
	python LSTM_multiftr.py

	Without arguments, Saves 395 days of past data
	in Features.csv and saves past 30 days of test
	data in file lstm_backtest.csv

2) With command line arguments:
	python LSTM_multiftr.py <SAMPLE SIZE> <VALIDATIONS DAYS> <TEST_DAYS>

	Saves past <SAMPLE SIZE> days of data in Features.csv
	Uses <VALIDATION DAYS> to validate trained model
	Tests on past <TEST_DAYS> and saves data in lstm_backtest.csv


FILES GENERATED
==========================================================================
- Features.csv: CSV file storing Bitcoin data fetched from Quandl. Parsed by the Python script
- lstm_backtest.csv: Test data in format Date|Actual Price on Date| Predicted Price for Date
- lstm_nextday.csv: Single value which is the rpedicted price of Bitcoin for next day from today [BROKEN- Needs to be fixed]

- LSTM_test.png: Plot showing prediction vs actual price over test data
- LSTM_validate.png: Plot showing prediction vs actual price when testing on validation data
- LSTM_valueloss_training.png: Showing valueloss during training and validation

Program Output
==========================================================================
On Console: Shows training epochs when training
On Console: Displays RMSE for validation and testing
On Console: Shows when removing old files and writing to new ones
In DIrectory: Saves Files mentioned in above section