import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd

# Function to plot the stock's close price with SMA and EMA
def plot_close_with_moving_averages(
    df, 
    date_col='Date', 
    close_col='Close', 
    sma_col='SMA_20', 
    ema_col='EMA_20', 
    num_rows=None
):
    """
    Plot the stock's close price along with its SMA and EMA, showing a fixed number of rows if specified.

    Parameters:
        df (pd.DataFrame): The DataFrame containing stock data.
        date_col (str): The column name for the date (default: 'Date').
        close_col (str): The column name for the close price (default: 'Close').
        sma_col (str): The column name for the Simple Moving Average (default: 'SMA_20').
        ema_col (str): The column name for the Exponential Moving Average (default: 'EMA_20').
        num_rows (int, optional): The number of rows to display in the chart (default: None, shows all data).
    """
    if num_rows is not None:
        df = df.tail(num_rows)
    
    plt.figure(figsize=(14, 7))
    plt.plot(df[date_col], df[close_col], label='Close Price', linewidth=1.5)
    
    if sma_col in df.columns:
        plt.plot(df[date_col], df[sma_col], label=f'{sma_col}', linestyle='--')
    
    if ema_col in df.columns:
        plt.plot(df[date_col], df[ema_col], label=f'{ema_col}', linestyle='-.')
    
    plt.title('Close Price with SMA and EMA')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()


# Function to plot the stock's close price with Bollinger Bands
def plot_bollinger_bands(
    df, 
    date_col='Date', 
    close_col='Close', 
    upper_band='BB_upper', 
    lower_band='BB_lower', 
    middle_band='BB_middle', 
    num_rows=None
):
    """
    Plot the stock's close price along with Bollinger Bands, showing a fixed number of rows if specified.

    Parameters:
        df (pd.DataFrame): The DataFrame containing stock data.
        date_col (str): The column name for the date (default: 'Date').
        close_col (str): The column name for the close price (default: 'Close').
        upper_band (str): The column name for the upper Bollinger Band.
        lower_band (str): The column name for the lower Bollinger Band.
        middle_band (str): The column name for the middle Bollinger Band.
        num_rows (int, optional): The number of rows to display in the chart (default: None, shows all data).
    """
    if num_rows is not None:
        df = df.tail(num_rows)
    
    plt.figure(figsize=(14, 7))
    plt.plot(df[date_col], df[close_col], label='Close Price', linewidth=1.5)
    
    if upper_band in df.columns and lower_band in df.columns:
        plt.plot(df[date_col], df[upper_band], label='Bollinger Upper Band', linestyle='--')
        plt.plot(df[date_col], df[middle_band], label='Bollinger Middle Band', linestyle='-.')
        plt.plot(df[date_col], df[lower_band], label='Bollinger Lower Band', linestyle='--')
        plt.fill_between(df[date_col], df[lower_band], df[upper_band], color='gray', alpha=0.2, label='Bollinger Bands')
    
    plt.title('Close Price with Bollinger Bands')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()


# Function to plot the RSI (Relative Strength Index)
def plot_rsi(
    df, 
    date_col='Date', 
    rsi_col='RSI', 
    num_rows=None
):
    """
    Plot the RSI for the stock, showing a fixed number of rows if specified.

    Parameters:
        df (pd.DataFrame): The DataFrame containing stock data.
        date_col (str): The column name for the date (default: 'Date').
        rsi_col (str): The column name for the RSI (default: 'RSI').
        num_rows (int, optional): The number of rows to display in the chart (default: None, shows all data).
    """
    if num_rows is not None:
        df = df.tail(num_rows)
    
    plt.figure(figsize=(14, 5))
    plt.plot(df[date_col], df[rsi_col], label='RSI', color='purple')
    plt.axhline(70, color='red', linestyle='--', linewidth=1, label='Overbought (70)')
    plt.axhline(30, color='green', linestyle='--', linewidth=1, label='Oversold (30)')
    plt.title('Relative Strength Index (RSI)')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.legend()
    plt.show()


# Function to plot the MACD (Moving Average Convergence Divergence)
def plot_macd(
    df, 
    date_col='Date', 
    macd_col='MACD', 
    signal_col='MACD_signal', 
    hist_col='MACD_hist', 
    num_rows=None
):
    """
    Plot the MACD line, signal line, and histogram, showing a fixed number of rows if specified.

    Parameters:
        df (pd.DataFrame): The DataFrame containing stock data.
        date_col (str): The column name for the date (default: 'Date').
        macd_col (str): The column name for the MACD line.
        signal_col (str): The column name for the Signal Line.
        hist_col (str): The column name for the Histogram.
        num_rows (int, optional): The number of rows to display in the chart (default: None, shows all data).
    """
    if num_rows is not None:
        df = df.tail(num_rows)
    
    plt.figure(figsize=(14, 7))
    plt.plot(df[date_col], df[macd_col], label='MACD', color='blue')
    plt.plot(df[date_col], df[signal_col], label='MACD Signal', color='orange')
    plt.bar(df[date_col], df[hist_col], label='MACD Histogram', color='gray', alpha=0.6)
    plt.title('MACD and Signal Line')
    plt.xlabel('Date')
    plt.ylabel('MACD Value')
    plt.legend()
    plt.show()


# Function to plot the candlestick chart
def plot_candlestick_chart(
    df,
    date_col='Date',
    resample_period=None,
    start_date=None,
    end_date=None,
    title='Candlestick Chart',
    mav=(10, 20),
    figsize=(14, 8),
    style='yahoo',
    auto_resample_threshold=300,
    annotations=None,
    num_rows=None
):
    """
    Plot a candlestick chart, showing a fixed number of rows if specified.

    Parameters:
        df (pd.DataFrame): The DataFrame containing stock data.
        date_col (str): The column name for the date (default: 'Date').
        resample_period (str): Resampling frequency ('W' for weekly, 'M' for monthly, etc.).
        start_date (str): Start date for filtering (e.g., '2023-01-01').
        end_date (str): End date for filtering (e.g., '2023-06-30').
        title (str): Title of the chart (default: 'Candlestick Chart').
        mav (tuple): Tuple of moving average periods to plot (default: (10, 20)).
        figsize (tuple): Size of the figure (default: (14, 8)).
        style (str): Chart style (default: 'yahoo').
        auto_resample_threshold (int): Automatically resample if the dataset has more rows than this value.
        annotations (list of tuples): List of annotations in the form [(date, label), ...].
        num_rows (int, optional): The number of rows to display in the chart (default: None, shows all data).
    """
    # Limit the number of rows if specified
    if num_rows is not None:
        df = df.tail(num_rows)
    
    # Ensure the Date column is in datetime format
    df[date_col] = pd.to_datetime(df[date_col])

    # Filter by date range if specified
    if start_date:
        df = df[df[date_col] >= start_date]
    if end_date:
        df = df[df[date_col] <= end_date]

    # Automatically resample if dataset is too large
    if len(df) > auto_resample_threshold and not resample_period:
        resample_period = 'W'

    # Resample data if resample_period is specified
    if resample_period:
        df = df.resample(resample_period, on=date_col).agg({
            'Open': 'first',
            'High': 'max',
            'Low': 'min',
            'Close': 'last',
            'Volume': 'sum'
        }).dropna()

    # Set Date column as the index for mplfinance
    df.set_index(date_col, inplace=True)

    # Add annotations to the chart
    add_plots = []
    if annotations:
        for date, label in annotations:
            add_plots.append(
                mpf.make_addplot(
                    [df.loc[date, 'Close']], type='scatter', markersize=100, marker='^', color='red', secondary_y=False
                )
            )

    # Prepare arguments for mplfinance plot
    plot_args = {
        'data': df,
        'type': 'candle',
        'volume': True,
        'style': style,
        'title': title,
        'figsize': figsize,
        'mav': mav,
    }
    if add_plots:  # Include addplot only if annotations exist
        plot_args['addplot'] = add_plots

    # Plot the candlestick chart
    mpf.plot(**plot_args)

