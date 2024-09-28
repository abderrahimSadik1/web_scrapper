from flask import Flask,request,render_template
from cnbcScrapper import scrape_cnbc
from sentimentAnalysis import sentiment_analysis
from stocks import update_stock_price
import pandas as pd
app = Flask(__name__)

@app.route('/')
def index():
    # Load the CSV data
    data = pd.read_csv('data/companies.csv')
    return render_template('index.html', data=data)

@app.route('/update')
def update():
    headlines = scrape_cnbc()
    for headline in headlines:
        sentiment_analysis(headline.text)
    return 'Data updated successfully'

if __name__ == '__main__':
    app.run(debug=True)