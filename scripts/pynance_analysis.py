import pandas as pd
import pynance as pn
import matplotlib.pyplot as plt
import mplfinance as mpf


# Data Loading


def fetch_data(symbol, start_date, end_date):
    """
    Fetch stock price data using PyNance.

    Parameters:
        symbol (str): Stock symbol (e.g., 'AAPL').
        start_date (str): Start date (YYYY-MM-DD).
        end_date (str): End date (YYYY-MM-DD).

    Returns:
        pd.DataFrame: Stock price data.
    """
    data = pn.data.get(symbol, start=start_date, end=end_date)
    data.reset_index(inplace=True)  # Ensure Date is a column
    data['Date'] = pd.to_datetime(data['Date'])  # Ensure Date is in datetime format
    return data


# Technical Indicators


def calculate_indicators(data):
    """
    Calculate technical indicators manually using Pandas.

    Parameters:
        data (pd.DataFrame): Stock price data.

    Returns:
        pd.DataFrame: DataFrame with added indicators.
    """
    # Ensure the 'Close' column exists
    if 'Close' not in data.columns:
        raise KeyError("The 'Close' column is missing in the data.")

    # Simple Moving Average (SMA)
    data['SMA_20'] = data['Close'].rolling(window=20).mean()

    # Exponential Moving Average (EMA)
    data['EMA_20'] = data['Close'].ewm(span=20, adjust=False).mean()

    # Relative Strength Index (RSI)
    delta = data['Close'].diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))

    # Bollinger Bands
    data['BB_middle'] = data['Close'].rolling(window=20).mean()
    data['BB_std'] = data['Close'].rolling(window=20).std()
    data['BB_upper'] = data['BB_middle'] + 2 * data['BB_std']
    data['BB_lower'] = data['BB_middle'] - 2 * data['BB_std']
    data.drop(columns=['BB_std'], inplace=True)

    # MACD (Moving Average Convergence Divergence)
    ema_12 = data['Close'].ewm(span=12, adjust=False).mean()
    ema_26 = data['Close'].ewm(span=26, adjust=False).mean()
    data['MACD'] = ema_12 - ema_26
    data['MACD_signal'] = data['MACD'].ewm(span=9, adjust=False).mean()
    data['MACD_hist'] = data['MACD'] - data['MACD_signal']

    # Handle NaN values
    data = handle_nan_values(data)

    return data


def handle_nan_values(data):
    """
    Handle NaN values in the DataFrame by dropping or filling them.

    Parameters:
        data (pd.DataFrame): DataFrame with NaN values.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    # Drop rows where any indicator is NaN
    data = data.dropna()

    # Alternatively, you can fill NaN values with placeholders:
    # data.fillna(0, inplace=True)

    return data


# Visualization Functions


def plot_close_with_indicators(data):
    """
    Plot Close Price with SMA and EMA.
    """
    plt.figure(figsize=(14, 7))
    plt.plot(data['Date'], data['Close'], label='Close Price', linewidth=1.5)
    plt.plot(data['Date'], data['SMA_20'], label='SMA 20', linestyle='--')
    plt.plot(data['Date'], data['EMA_20'], label='EMA 20', linestyle='-.')
    plt.title('Close Price with SMA and EMA')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()


def plot_rsi(data):
    """
    Plot RSI.
    """
    plt.figure(figsize=(14, 5))
    plt.plot(data['Date'], data['RSI'], label='RSI', color='purple')
    plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
    plt.axhline(30, color='green', linestyle='--', label='Oversold (30)')
    plt.title('RSI (Relative Strength Index)')
    plt.legend()
    plt.show()


def plot_macd(data):
    """
    Plot MACD, Signal Line, and Histogram.
    """
    plt.figure(figsize=(14, 7))
    plt.plot(data['Date'], data['MACD'], label='MACD', color='blue')
    plt.plot(data['Date'], data['MACD_signal'], label='Signal Line', color='orange')
    plt.bar(data['Date'], data['MACD_hist'], label='Histogram', color='gray', alpha=0.6)
    plt.title('MACD and Signal Line')
    plt.legend()
    plt.show()


def plot_bollinger_bands(data):
    """
    Plot Close Price with Bollinger Bands.
    """
    plt.figure(figsize=(14, 7))
    plt.plot(data['Date'], data['Close'], label='Close Price', linewidth=1.5)
    plt.plot(data['Date'], data['BB_upper'], label='BB Upper', linestyle='--')
    plt.plot(data['Date'], data['BB_lower'], label='BB Lower', linestyle='--')
    plt.fill_between(data['Date'], data['BB_lower'], data['BB_upper'], color='gray', alpha=0.2)
    plt.title('Close Price with Bollinger Bands')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()


def plot_candlestick_chart(data):
    """
    Plot Candlestick Chart with mplfinance.
    """
    data.set_index('Date', inplace=True)
    mpf.plot(data, type='candle', volume=True, style='yahoo', mav=(10, 20))
    data.reset_index(inplace=True)  # Restore the original index



# Main Workflow

if __name__ == "__main__":
    # Define the stock symbol and date range
    symbol = 'AAPL'
    start_date = '2023-01-01'
    end_date = '2023-12-31'

    # Fetch the stock data
    data = fetch_data(symbol, start_date, end_date)

    # Calculate indicators
    data = calculate_indicators(data)

    # Visualize the data and indicators
    plot_close_with_indicators(data)
    plot_rsi(data)
    plot_macd(data)
    plot_bollinger_bands(data)
    plot_candlestick_chart(data)

    
