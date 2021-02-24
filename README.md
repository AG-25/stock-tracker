This program does the following:  
1.) Collects daily stock market price data for a company (the stock ticker and company name should be provided by the user).  
2.) Compares the percentage price change of the stock in the last day to an "ALLOWABLE_PERCENT" variable.  
3.) Extracts breaking news and sends URLs for the breaking news articles to the user in an SMS message if the percentage price fluctuation exceeds ALLOWABLE_PERCENT.  
  
The following free APIs are used:  
Alphavantage (for stock price data) - https://www.alphavantage.co/  
NewsAPI (for breaking news articles about the stock) - https://newsapi.org/  
Twilio (for sending SMS messages) - https://www.twilio.com/  
  
The following environment variables need to be provided for the script to work:  
ALPHAVANTAGE_API_KEY, NEWS_API_KEY, TWILIO_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER - These can be retrieved by signing up for the free APIs at the URLs provided above.  
RECIPIENT_PHONE_NUMBER - This is the phone number that SMS messages about the stock should be sent to (e.g. the mobile number of the script user).
