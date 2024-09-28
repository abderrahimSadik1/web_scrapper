import pandas as pd
from textblob import TextBlob
from stocks import update_stock_price

def sentiment_analysis(headline):
    # Load data
    data = pd.read_csv('data/companies.csv')

    # Split the sentence into individual words
    words = headline.lower().split()

    # Check if any word in the sentence exists in the column
    companies = data[data['companies'].apply(lambda x: any(str(x).lower() in company for company in words))]

    # If any word exists, perform sentiment analysis
    if(len(companies) != 0):
        blob = TextBlob(headline)
        if blob.sentiment.polarity > 0:
            sentiment_score = f'{blob.sentiment.polarity:.2f} (Positive)'
        elif blob.sentiment.polarity < 0:
            sentiment_score = f'{blob.sentiment.polarity:.2f} (Negative)'
        else:
            sentiment_score = f'{blob.sentiment.polarity:.2f} (Neutral)'
        # Update the data with the sentiment score
        data.loc[data['companies'].isin(companies['companies']), ['sentiment score', 'new headline']] = sentiment_score, headline
        update_stock_price(companies['symbol'].values[0])
    data.to_csv('data/companies.csv', index=False)



