# GeminiCode
Alert Monitoring Tool for Gemini Test


Program is written in Python3

Prerequisite:-
==========

1.  Install Virtual Environment

	python3 -m pip install --user virtualenv

2. Create a Virtual Environment 

	python3 -m venv environment

3. Activate Environment
Move to the parent folder where the “environment” virtual environment was created and issue following command:-

	source environment/bin/activate

4. Load all the prerequisite package by going into “GeminiCode” folder and locate “requirement.txt” file:-

	pip install -r requirement.txt

Executing program:-
===============

1. Change directory to GeminiCode folder and execute following command to see all the options:-

	python main.py -h

 	Snippet:-

	(venv) shankars-mbp:GeminiCode shankarkrishnamurthy$ python main.py -h
	2021-11-28 19:36:08,637 - AlertingTool - INFO - Parsing Command Line Arguments
	usage: main.py [-h] --currency CURRENCY --type TYPE [--deviation DEVIATION]

	optional arguments:
 	 -h, --help            show this help message and exit
  	 --currency CURRENCY, -c CURRENCY
                        Currency The currency trading pair, or ALL
  	 --type TYPE, -t TYPE  {pricedev,pricechange,voldev,ALL} The type of check to run, or ALL
  	 --deviation DEVIATION, -d DEVIATION
                        Deviation percentage deviation of the change

2. Executing Program:-

Program requires two required parameters - “currency” and “type”. One optional parameter “deviation”.

--currency or -c:
  Input Options:
	-  Currency name
	- ALL : if alert is needed for all currencies
--type or -t:
  Input Options:
	- pricedev : Generate an alert if the current price is more than x standard deviation from the 24hr average
	- pricechange : Generate an alert if the current price has changed in the past 24 hours by more than X% from the price at the start of the period
	- volchange : Generate an alert if the quantity of the most recent trade is more than X% of the total 24hr volume in the symbol
	- ALL : Execute all 3 functions - pricedev, pricechange, volchange
--deviation or -d:
	Input: float  -  Threshold passed for each function. If no value is passed default value of 1.0 is used.

	Snippet:-
	
	(venv) shankars-mbp:GeminiCode shankarkrishnamurthy$ python main.py -c btcusd -t pricedev -d 10.0
	2021-11-28 19:50:42,897 - AlertingTool - INFO - Parsing Command Line Arguments
	2021-11-28 19:50:42,897 - AlertingTool - INFO - Fetching API data for currency btcusd
	2021-11-28 19:50:43,123 - AlertingTool - INFO - Running Standard Deviation check on btcusd
	2021-11-28 19:50:43,123 - AlertingTool - ERROR - Price Deviation: Currency BTCUSD Standard Deviation Change 794.2126448650811

	
	(venv) shankars-mbp:GeminiCode shankarkrishnamurthy$ python main.py -c btcusd -t pricechange -d 0.01
	2021-11-28 19:51:34,172 - AlertingTool - INFO - Parsing Command Line Arguments
	2021-11-28 19:51:34,420 - AlertingTool - INFO - Requesting PriceFeed API Data
	2021-11-28 19:51:34,420 - AlertingTool - INFO - Running checks to see if PriceChange Alert is met.
	2021-11-28 19:51:34,420 - AlertingTool - ERROR - Currency is BTCUSD 
 	Percent Change 0.0562
	
	(venv) shankars-mbp:GeminiCode shankarkrishnamurthy$ python main.py -c btcusd -t voldev -d 0.01
	2021-11-28 19:52:38,359 - AlertingTool - INFO - Parsing Command Line Arguments
	2021-11-28 19:52:38,360 - AlertingTool - INFO - Fetching API data for currency btcusd
	2021-11-28 19:52:38,538 - AlertingTool - INFO - Fetching Volume in USD
	2021-11-28 19:52:38,538 - AlertingTool - INFO - Getting most recent trade information
	2021-11-28 19:52:38,538 - AlertingTool - INFO - Checking for volume deviation for currency btcusd
	2021-11-28 19:52:38,538 - AlertingTool - ERROR - Volume Deviation: Currency btcusd - Quantity of most recent trade is greater than 0.010000 of the total volume
	(venv) shankars-mbp:GeminiCode shankarkrishnamurthy$ python main.py -c ALL -t pricechange -d 0.01
	2021-11-28 20:19:41,403 - AlertingTool - INFO - Parsing Command Line Arguments
	2021-11-28 20:19:42,318 - AlertingTool - INFO - Requesting PriceFeed API Data
	2021-11-28 20:19:42,318 - AlertingTool - INFO - Running checks to see if PriceChange Alert is met.
	2021-11-28 20:19:42,318 - AlertingTool - ERROR - Currency is BTCGBP 
 	Percent Change 0.0586
	2021-11-28 20:19:42,318 - AlertingTool - ERROR - Currency is MATICUSD 
 	Percent Change 0.0442
	2021-11-28 20:19:42,318 - AlertingTool - ERROR - Currency is STORJUSD 
	 Percent Change 0.0678
	2021-11-28 20:19:42,319 - AlertingTool - ERROR - Currency is ETHUSD 
	 Percent Change 0.0689
	2021-11-28 20:19:42,319 - AlertingTool - ERROR - Currency is UNIUSD 
 	Percent Change 0.0483
	2021-11-28 20:19:42,319 - AlertingTool - ERROR - Currency is CRVUSD 
	 Percent Change 0.0518
	2021-11-28 20:19:42,319 - AlertingTool - ERROR - Currency is ETHEUR 
	 Percent Change 0.0735
	2021-11-28 20:19:42,319 - AlertingTool - ERROR - Currency is KNCUSD 
	 Percent Change 0.0203
	2021-11-28 20:19:42,319 - AlertingTool - ERROR - Currency is ALCXUSD 
 	Percent Change 0.2790
	2021-11-28 20:19:42,319 - AlertingTool - ERROR - Currency is AXSUSD 
 	Percent Change 0.0722
	2021-11-28 20:19:42,320 - AlertingTool - ERROR - Currency is CUBEUSD 
	 Percent Change 0.1085
	2021-11-28 20:19:42,320 - AlertingTool - ERROR - Currency is OXTUSD 
	 Percent Change 0.0108
	2021-11-28 20:19:42,320 - AlertingTool - ERROR - Currency is ETHSGD 
	 Percent Change 0.0638
	2021-11-28 20:19:42,320 - AlertingTool - ERROR - Currency is LINKUSD 
	 Percent Change 0.0386
	2021-11-28 20:19:42,320 - AlertingTool - ERROR - Currency is WCFGUSD 
 	Percent Change 0.0433
	2021-11-28 20:19:42,320 - AlertingTool - ERROR - Currency is BTCEUR 
 	Percent Change 0.0608
	2021-11-28 20:19:42,320 - AlertingTool - ERROR - Currency is DOGEUSD 
 	Percent Change 0.0230
	2021-11-28 20:19:42,320 - AlertingTool - ERROR - Currency is BCHUSD 
 	Percent Change 0.0238
	2021-11-28 20:19:42,320 - AlertingTool - ERROR - Currency is SLPUSD 
 	Percent Change 0.0379
	2021-11-28 20:19:42,320 - AlertingTool - ERROR - Currency is AMPUSD 
	 Percent Change 0.0706
	2021-11-28 20:19:42,320 - AlertingTool - ERROR - Currency is BTCUSD 
	 Percent Change 0.0602
	2021-11-28 20:19:42,320 - AlertingTool - ERROR - Currency is LTCUSD 
	Percent Change 0.0401
	2021-11-28 20:19:42,320 - AlertingTool - ERROR - Currency is BTCDAI 
	 Percent Change 0.0545
	2021-11-28 20:19:42,321 - AlertingTool - ERROR - Currency is RAREUSD 
 	Percent Change 0.0484
	2021-11-28 20:19:42,321 - AlertingTool - ERROR - Currency is LTCBCH 
	 Percent Change 0.0168
	 
	 (venv) shankars-mbp:GeminiCode shankarkrishnamurthy$ python main.py -c btcusd -t ALL -d 0.01
	2021-11-28 20:23:24,390 - AlertingTool - INFO - Parsing Command Line Arguments
	2021-11-28 20:23:24,391 - AlertingTool - INFO - Calling pricechange module
	2021-11-28 20:23:24,910 - AlertingTool - INFO - Requesting PriceFeed API Data
	2021-11-28 20:23:24,911 - AlertingTool - INFO - Running checks to see if PriceChange Alert is met.
	2021-11-28 20:23:24,911 - AlertingTool - ERROR - Currency is BTCUSD 
 	Percent Change 0.0608
	2021-11-28 20:23:24,911 - AlertingTool - INFO - Calling standard deviation module
	2021-11-28 20:23:24,911 - AlertingTool - INFO - Fetching API data for currency btcusd
	2021-11-28 20:23:25,180 - AlertingTool - INFO - Running Standard Deviation check on btcusd
	2021-11-28 20:23:25,180 - AlertingTool - ERROR - Price Deviation: Currency BTCUSD Standard Deviation Change 1019.8457590314791
	2021-11-28 20:23:25,181 - AlertingTool - INFO - Calling Volume deviation
	2021-11-28 20:23:25,181 - AlertingTool - INFO - Fetching API data for currency btcusd
	2021-11-28 20:23:25,444 - AlertingTool - INFO - Fetching Volume in USD
	2021-11-28 20:23:25,445 - AlertingTool - INFO - Getting most recent trade information
	2021-11-28 20:23:25,445 - AlertingTool - INFO - Checking for volume deviation for currency btcusd
	2021-11-28 20:23:25,445 - AlertingTool - ERROR - Volume Deviation: Currency btcusd - Quantity of most recent trade is greater than 0.010000 of the total volume

Improvements:-
===========

1. Add flexibility to call these functions using rest API call and return alerts via JSON.

2. Write the logs in a file so that it could be retrieved later.

Approach:-
========

- Read Gemini API doc to see which API calls are needed to execute our functions. 
- Added logic to handle all cases for all scenarios and throw exceptions for any errors.
- I followed all the rules of Object oriented Programming and made sure the program is modular and reusable.


Time it took:-
============

3 hours
