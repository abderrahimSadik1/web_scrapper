# Tech Market News Scraper and Sentiment Analysis

This project is a web scraping tool designed to extract news article titles related to the technology market, perform sentiment analysis, and retrieve real-time stock market prices. It’s built using **Flask** for the web interface and **TextBlob** for sentiment analysis.
![image](https://github.com/user-attachments/assets/ba4b6a27-232f-47fc-a5c2-c046357ed107)


## Features

- Scrapes headlines and news article titles from [CNBC Technology](https://www.cnbc.com/technology/).
- Performs sentiment analysis on the scraped titles using **TextBlob**.
- Fetches real-time stock prices for companies using the **Polygon API**.
- Flask-based web interface to display the results.
- **Adding Companies:** To add a new company, update the `companies.csv` file with the company name and its stock symbol.

## Installation

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Add your Polygon API key to the `stocks.py` file:
   ```python
   api_key = 'YOUR_POLYGON_API_KEY'
   ```

## Usage

- Run the Flask application:
   ```bash
   python app.py
   ```
   
- Access the web interface by navigating to `http://127.0.0.1:5000` in your browser.

## API Key

This project requires a **Polygon API** key to fetch real-time stock data. You can obtain an API key from [Polygon.io](https://polygon.io/).



