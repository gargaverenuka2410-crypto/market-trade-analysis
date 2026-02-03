import pandas as pd
import os

def load_trader_data(file_path):
    """
     Loads Hyper-liquid trade data and handles basic integrity checks.
    """
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return None
    
    # Load data
    df = pd.read_csv(file_path)
    
    # Logic: Convert timestamp to datetime objects
    # Note: Use errors='coerce' to handle corrupt timestamps
    df['time'] = pd.to_datetime(df['time'], errors='coerce')
    
    # Logic: Drop rows where PnL is missing (Data Integrity check)
    df = df.dropna(subset=['closedPnL'])
    
    print(f"Successfully loaded {len(df)} trade records.")
    return df

def load_sentiment_data(file_path):
    """
    Loads Bitcoin Fear & Greed index and cleans the date format.
    """
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return None
    
    df = pd.read_csv(file_path)
    
    # Logic: Standardize Date format to match trade data for merging
    df['Date'] = pd.to_datetime(df['Date']).dt.date
    
    return df

# Example usage (Uncomment to test):
# trades = load_trader_data('data/trades.csv')
# sentiment = load_sentiment_data('data/sentiment.csv')
