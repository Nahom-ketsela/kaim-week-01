import pandas as pd
import os

def load_stock_data(file_path: str) -> pd.DataFrame:
    """
    Load stock price data from a CSV file into a pandas DataFrame.
    
    Parameters:
        file_path (str): Path to the CSV file containing stock price data.
        
    Returns:
        pd.DataFrame: DataFrame containing the stock price data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    
    data = pd.read_csv(file_path)
    
    # Check if essential columns are present
    required_columns = {'Open', 'High', 'Low', 'Close', 'Volume'}
    if not required_columns.issubset(data.columns):
        raise ValueError(f"The input data must contain these columns: {required_columns}")
    
    return data


def prepare_stock_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare and clean stock price data.
    
    Parameters:
        df (pd.DataFrame): Raw stock price data.
        
    Returns:
        pd.DataFrame: Cleaned and prepared stock price data.
    """
    # Ensure there are no missing values
    df = df.dropna()
    
    # Convert date column to datetime if it exists
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.sort_values(by='Date')
    
    # Reset the index
    df = df.reset_index(drop=True)
    
    return df

def add_daily_return(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a daily return column to the DataFrame.
    
    Parameters:
        df (pd.DataFrame): Stock price data.
        
    Returns:
        pd.DataFrame: DataFrame with the daily return column added.
    """
    df['Daily_Return'] = df['Close'].pct_change()
    return df
