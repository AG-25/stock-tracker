# Stock Tracker

This is a program which tracks the daily closing price of a stock and sends an alert SMS to the user when the price fluctuates by more than a specified percentage. A list of breaking news articles for the stock are included in the SMS.

## How the Application Works
1. Collects daily stock price data from the Alphavantage API (the stock ticker and company name should be provided by the user).  
1. Compares the percentage price change of the stock in the last day to an "ALLOWABLE_PERCENT" variable.  
1. If the percentage change exceeds ALLOWABLE_PERCENT, then an SMS warning is sent to the user which includes breaking news articles about the company. The news is extracted from the NewsAPI.

## Using the Application
Download main.py and install the modules listed in requirements.txt using pip (twilio and requests).  
<br>
The following environment variables should then be populated before running the program:
* ALPHAVANTAGE_API_KEY, NEWS_API_KEY, TWILIO_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER - Values for these variables can be retrieved by signing up for the free APIs at the URLs provided below.
* RECIPIENT_PHONE_NUMBER - This is the phone number that SMS messages about the stock should be sent to (e.g. the mobile number of the script user).

## Supporting Libraries and APIs
* Alphavantage (for stock price data) - https://www.alphavantage.co/  
* NewsAPI (for breaking news articles about the stock) - https://newsapi.org/  
* Twilio (for sending SMS messages) - https://www.twilio.com/  
