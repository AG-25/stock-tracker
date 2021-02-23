import requests
from twilio.rest import Client
import os

# The ticker, company name and allowable % daily price fluctuation of the stock
# which will be tracked. An SMS will be sent when the stock price changes by
# more than ALLOWABLE_PERCENT.
COMPANY_NAME = "APPLE"
TICKER = "AAPL"
ALLOWABLE_PERCENT = 2

# Extracting API keys and AUTH tokens from environment variables
ALPHAVANTAGE_API_KEY = os.getenv('ALPHAVANTAGE_API_KEY')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
RECIPIENT_PHONE_NUMBER = os.getenv('RECIPIENT_PHONE_NUMBER')

ALPHAVANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
ALPHAVANTAGE_PARAMS = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': TICKER,
    'apikey': ALPHAVANTAGE_API_KEY,
}
NEWS_ENDPOINT = 'http://newsapi.org/v2/everything'
NEWS_PARAMS = {
    'q': TICKER,
    'sortBy': 'popularity',
    'language': 'en',
    'qInTitle': COMPANY_NAME,
    'apiKey': NEWS_API_KEY,
}

# Get stock price data and calculate the % change from the previous day
response = requests.get(
    url=ALPHAVANTAGE_ENDPOINT, params=ALPHAVANTAGE_PARAMS
)
price_data = response.json()['Time Series (Daily)']
close_prices = [float(price_data[date]['4. close']) for date in price_data]
pct_change = 100 * ((close_prices[1] - close_prices[0]) / close_prices[1])
pct_change = round(pct_change, 2)

# If the % change exceeds ALLOWABLE_PERCENT then retrieve recent news articles
# and send an SMS using the Twilio API
if abs(pct_change) > ALLOWABLE_PERCENT:
    response = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMS)
    news_articles = response.json()['articles']
    if pct_change > 0:
        change_symbol = '🔺'
    else:
        change_symbol = '🔻'

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in news_articles[:3]:
        headline = article['title']
        brief = article['description']
        message = client.messages \
            .create(
                body=f"{TICKER}: {change_symbol}{pct_change}% "
                     f"\n Headline: {headline} "
                     f"\n Brief: {brief}",
                from_=TWILIO_PHONE_NUMBER,
                to=RECIPIENT_PHONE_NUMBER,
            )
        print(message.status)
