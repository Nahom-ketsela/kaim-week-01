import pandas as pd
import talib

# Function to ensure required columns exist in the DataFrame
def validate_columns(df: pd.DataFrame, required_columns: set):
    """
    Validate that the DataFrame contains the required columns.
    
    Parameters:
        df (pd.DataFrame): DataFrame to validate.
        required_columns (set): Set of required column names.
        
    Raises:
        ValueError: If required columns are missing.
    """
    if not required_columns.issubset(df.columns):
        raise ValueError(f"The DataFrame must contain these columns: {required_columns}")

# Moving Averages
def add_sma(df: pd.DataFrame, period: int = 20) -> pd.DataFrame:
    df[f'SMA_{period}'] = talib.SMA(df['Close'], timeperiod=period)
    return df

def add_ema(df: pd.DataFrame, period: int = 20) -> pd.DataFrame:
    df[f'EMA_{period}'] = talib.EMA(df['Close'], timeperiod=period)
    return df

# RSI (Relative Strength Index)
def add_rsi(df: pd.DataFrame, period: int = 14) -> pd.DataFrame:
    df['RSI'] = talib.RSI(df['Close'], timeperiod=period)
    return df

# MACD (Moving Average Convergence Divergence)
def add_macd(df: pd.DataFrame) -> pd.DataFrame:
    df['MACD'], df['MACD_signal'], df['MACD_hist'] = talib.MACD(
        df['Close'], fastperiod=12, slowperiod=26, signalperiod=9
    )
    return df

# Bollinger Bands
def add_bollinger_bands(df: pd.DataFrame, period: int = 20) -> pd.DataFrame:
    df['BB_upper'], df['BB_middle'], df['BB_lower'] = talib.BBANDS(
        df['Close'], timeperiod=period, nbdevup=2, nbdevdn=2, matype=0
    )
    return df

# Average True Range (ATR)
def add_atr(df: pd.DataFrame, period: int = 14) -> pd.DataFrame:
    df['ATR'] = talib.ATR(df['High'], df['Low'], df['Close'], timeperiod=period)
    return df

# Stochastic Oscillator
def add_stochastic_oscillator(df: pd.DataFrame) -> pd.DataFrame:
    df['SlowK'], df['SlowD'] = talib.STOCH(
        df['High'], df['Low'], df['Close'], 
        fastk_period=14, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0
    )
    return df

# Wrapper Function to Add All Indicators
def calculate_technical_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Wrapper function to calculate and add all technical indicators to the DataFrame.
    
    Parameters:
        df (pd.DataFrame): Stock price data with 'Close', 'Open', 'High', 'Low', and 'Volume' columns.
        
    Returns:
        pd.DataFrame: DataFrame with added technical indicators.
    """
    required_columns = {'Open', 'High', 'Low', 'Close', 'Volume'}
    validate_columns(df, required_columns)
    
    df = add_sma(df)
    df = add_ema(df)
    df = add_rsi(df)
    df = add_macd(df)
    df = add_bollinger_bands(df)
    df = add_atr(df)
    df = add_stochastic_oscillator(df)
    
    return df
