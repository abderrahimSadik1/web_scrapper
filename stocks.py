import requests
import pandas as pd
from datetime import datetime,timedelta

def update_stock_price(symbol):
    # Load data
    data = pd.read_csv('data/companies.csv')

    # date of the trading session
    date = datetime.now().date()- timedelta(days=1)

    # Polygon API key
    polygon_api_key = 'YOUR_POLYGON_API_KEY'
    sym = symbol.upper()
    # api url
    URL = f'https://api.polygon.io/v1/open-close/{sym}/{date}?adjusted=true&apiKey={polygon_api_key}'
    response = requests.get(URL)

    if response.status_code == 200:
        # Extract data from the response
        stock_data= response.json()
        open_price = stock_data['open']
        close_price = stock_data['close']
        high_price = stock_data['high']
        low_price = stock_data['low']
        volume = stock_data['volume']

        # Update the data
        data.loc[data['symbol'] == symbol, ['open','close','high','low','volume','trading session date']] = open_price,close_price,high_price,low_price,volume,date
    else:
        print(f'Failed to fetch data for {sym} {response.status_code}')
    data.to_csv('data/companies.csv', index=False)
