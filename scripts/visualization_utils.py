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


