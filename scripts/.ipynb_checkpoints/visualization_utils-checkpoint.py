import matplotlib.pyplot as plt
import mplfinance as mpf

def plot_close_with_moving_averages(df, date_col='Date', close_col='Close', sma_col='SMA_20', ema_col='EMA_20'):
    """
    Plot the stock's close price along with its SMA and EMA.
    """
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


def plot_bollinger_bands(df, date_col='Date', close_col='Close', upper_band='BB_upper', lower_band='BB_lower', middle_band='BB_middle'):
    """
    Plot the stock's close price along with Bollinger Bands.
    """
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


def plot_rsi(df, date_col='Date', rsi_col='RSI'):
    """
    Plot the Relative Strength Index (RSI) for the stock.
    """
    plt.figure(figsize=(14, 5))
    plt.plot(df[date_col], df[rsi_col], label='RSI', color='purple')
    plt.axhline(70, color='red', linestyle='--', linewidth=1, label='Overbought (70)')
    plt.axhline(30, color='green', linestyle='--', linewidth=1, label='Oversold (30)')
    plt.title('Relative Strength Index (RSI)')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.legend()
    plt.show()


def plot_macd(df, date_col='Date', macd_col='MACD', signal_col='MACD_signal', hist_col='MACD_hist'):
    """
    Plot the MACD line, signal line, and histogram.
    """
    plt.figure(figsize=(14, 7))
    plt.plot(df[date_col], df[macd_col], label='MACD', color='blue')
    plt.plot(df[date_col], df[signal_col], label='MACD Signal', color='orange')
    plt.bar(df[date_col], df[hist_col], label='MACD Histogram', color='gray', alpha=0.6)
    plt.title('MACD and Signal Line')
    plt.xlabel('Date')
    plt.ylabel('MACD Value')
    plt.legend()
    plt.show()


def plot_close_and_volume(df, date_col='Date', close_col='Close', volume_col='Volume'):
    """
    Plot the stock's close price and trading volume on dual axes.
    """
    fig, ax1 = plt.subplots(figsize=(14, 7))

    # Plot close price
    ax1.plot(df[date_col], df[close_col], label='Close Price', color='blue', linewidth=1.5)
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Close Price', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    # Plot volume on a secondary y-axis
    ax2 = ax1.twinx()
    ax2.bar(df[date_col], df[volume_col], label='Volume', color='gray', alpha=0.3)
    ax2.set_ylabel('Volume', color='gray')
    ax2.tick_params(axis='y', labelcolor='gray')

    fig.suptitle('Close Price and Volume')
    fig.tight_layout()
    plt.show()


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
    annotations=None
):
    """
    Enhanced candlestick chart function for better visualization.

    Parameters:
        df (pd.DataFrame): DataFrame containing stock data with 'Open', 'High', 'Low', 'Close', and 'Volume'.
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
    """
    # Ensure the Date column is in datetime format
    df[date_col] = pd.to_datetime(df[date_col])

    # Filter by date range if specified
    if start_date:
        df = df[df[date_col] >= start_date]
    if end_date:
        df = df[df[date_col] <= end_date]

    # Automatically resample if dataset is too large
    if len(df) > auto_resample_threshold and not resample_period:
        resample_period = 'W'  # Default to weekly resampling if not provided

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

    # Plot the candlestick chart
    mpf.plot(
        df,
        type='candle',
        volume=True,
        style=style,
        title=title,
        figsize=figsize,
        mav=mav,
        addplot=add_plots if annotations else None,
    )