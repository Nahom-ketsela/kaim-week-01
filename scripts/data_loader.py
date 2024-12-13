import pandas as pd

def load_data(file_path):
    """
    Loads a CSV file into a Pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    DataFrame: The loaded Pandas DataFrame.
    """
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        print("CSV file successfully loaded.")

        # Display the first few rows of the DataFrame
        print("Preview of the data:")
        print(df.head())

        return df

    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
    except pd.errors.ParserError:
        print("Error: The file could not be parsed as a valid CSV.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


