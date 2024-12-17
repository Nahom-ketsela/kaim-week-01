import pandas as pd
from textblob import TextBlob
from scipy.stats import pearsonr

# Function to load data
def load_data(stock_file, news_file):
    stock_data = pd.read_csv(stock_file)
    news_data = pd.read_csv(news_file)
    return stock_data, news_data

# Function to preprocess dates
def preprocess_dates(stock_data, news_data):
    """
    Normalize and align dates in stock and news data, ensuring valid datetime objects and uniform format.
    """
    # Parse stock_data['Date'] to datetime, ensuring it's in 'datetime64[ns]' format
    stock_data['Date'] = pd.to_datetime(stock_data['Date'], errors='coerce')

    # Parse news_data['date'], ensure the timezone is removed, and normalize
    news_data['date'] = pd.to_datetime(news_data['date'], errors='coerce')  # Ensure datetime conversion
    news_data['date'] = news_data['date'].dt.tz_localize(None)  # Remove timezone info
    news_data['date'] = news_data['date'].dt.normalize()  # Normalize to '00:00:00'

    # Drop rows with invalid dates (NaT)
    stock_data = stock_data.dropna(subset=['Date'])
    news_data = news_data.dropna(subset=['date'])

    # Ensure both columns are of 'datetime64[ns]' type
    stock_data['Date'] = stock_data['Date'].dt.tz_localize(None)
    news_data['date'] = news_data['date'].dt.tz_localize(None)

    # Standardize column names for merging
    stock_data.rename(columns={'Date': 'date'}, inplace=True)

    return stock_data, news_data

# Function to calculate daily returns for stock data
def calculate_daily_returns(stock_data):
    stock_data['daily_return'] = stock_data['Close'].pct_change() * 100
    return stock_data

# Function to perform sentiment analysis
def perform_sentiment_analysis(news_data):
    # Handle missing values in 'headline' by filling them with an empty string
    news_data['headline'] = news_data['headline'].fillna('')
    
    # Function to calculate sentiment polarity for a given text
    def get_sentiment(text):
        return TextBlob(text).sentiment.polarity
    
    # Vectorized way using list comprehension (faster than apply for large data)
    news_data['sentiment'] = [get_sentiment(x) for x in news_data['headline']]

    return news_data

# Function to aggregate daily sentiment scores
def aggregate_daily_sentiment(news_data):
    daily_sentiment = news_data.groupby('date')['sentiment'].mean().reset_index()
    return daily_sentiment

# Function to merge stock returns and daily sentiment
def merge_data(stock_data, daily_sentiment):
    # Ensure the column names match for merging
    merged_data = pd.merge(stock_data[['date', 'daily_return']], daily_sentiment, 
                           on='date', how='inner')
    return merged_data

# Function to calculate Pearson correlation
def calculate_correlation(merged_data):
    correlation, p_value = pearsonr(merged_data['sentiment'], merged_data['daily_return'])
    return correlation, p_value