import pandas as pd
import numpy as np

def calculate_daily_performance(df):
    """
    Logic: Aggregates trade data by Account and Date to create performance features.
    """
    # 1. Win Rate: Ratio of profitable trades to total trades
    # We create a boolean 'is_win' column first
    df['is_win'] = df['closedPnL'] > 0
    
    performance = df.groupby(['account', 'Date']).agg(
        total_trades=('closedPnL', 'count'),
        wins=('is_win', 'sum'),
        total_pnl=('closedPnL', 'sum'),
        avg_leverage=('leverage', 'mean'),  # Risk Appetite
        total_volume=('size', 'sum')        # Volume Profile
    ).reset_index()

    # Calculate Win Rate percentage
    performance['win_rate'] = (performance['wins'] / performance['total_trades']) * 100
    
    return performance

def segment_trader_tiers(df):
    """
    Logic: Segments traders into 'Whales' vs 'Retail' based on trade size.
    """
    # Logic: Using the 75th percentile to define Whales
    threshold = df['total_volume'].quantile(0.75)
    
    df['trader_tier'] = np.where(df['total_volume'] >= threshold, 'Whale', 'Retail')
    return df
