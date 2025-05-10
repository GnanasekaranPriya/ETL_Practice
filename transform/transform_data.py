import pandas as pd

def clean_orders(df):
    # Convert 'order_date' column to datetime
    df['order_date'] = pd.to_datetime(df['order_date'])
    
    # Fill any missing values in the 'amount' column with 0
    df['amount'] = df['amount'].fillna(0)
    
    # Create a new column 'amount_doubled' by doubling the 'amount'
    df['amount_doubled'] = df['amount'] * 2
    
    # Clean the 'status' column: convert to lowercase and strip any spaces
    df['status'] = df['status'].str.lower().str.strip()
    
    # Remove rows where 'amount' is less than or equal to 0
    df = df[df['amount'] > 0]
    
    # Create 'order_month' column as a string in "YYYY-MM" format from 'order_date'
    df['order_month'] = df['order_date'].dt.to_period('M').astype(str)
    
    return df
