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
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    news_data['date'] = pd.to_datetime(news_data['date'])
    return stock_data, news_data

# Function to calculate daily returns for stock data
def calculate_daily_returns(stock_data):
    stock_data['daily_return'] = stock_data['Close'].pct_change() * 100
    return stock_data

# Function to perform sentiment analysis
def perform_sentiment_analysis(news_data):
    news_data['sentiment'] = news_data['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    return news_data

# Function to aggregate daily sentiment scores
def aggregate_daily_sentiment(news_data):
    daily_sentiment = news_data.groupby('date')['sentiment'].mean().reset_index()
    return daily_sentiment

# Function to merge stock returns and daily sentiment
def merge_data(stock_data, daily_sentiment):
    merged_data = pd.merge(stock_data[['Date', 'daily_return']], daily_sentiment, 
                           left_on='Date', right_on='date', how='inner')
    return merged_data

# Function to calculate Pearson correlation
def calculate_correlation(merged_data):
    correlation, p_value = pearsonr(merged_data['sentiment'], merged_data['daily_return'])
    return correlation, p_value


