import pandas as pd
import os

# Correct path construction
base_path = os.path.join(os.path.dirname(__file__), '..', 'data')

nvidia_path = os.path.join(base_path, 'nvidia_data.csv')
bitcoin_path = os.path.join(base_path, 'bitcoin_data.csv')
merged_path = os.path.join(base_path, 'merged_data.csv')

# Load NVIDIA and Bitcoin data
nvidia = pd.read_csv(nvidia_path, parse_dates=['Date'])
bitcoin = pd.read_csv(bitcoin_path, parse_dates=['Date'])

nvidia['Date'] = pd.to_datetime(nvidia['Date'], utc=True).dt.tz_localize(None)
bitcoin['Date'] = pd.to_datetime(bitcoin['Date'], utc=True).dt.tz_localize(None)


# Preview loaded data
print("NVIDIA Data Preview:")
print(nvidia.head())
print("\nBitcoin Data Preview:")
print(bitcoin.head())

# Ensure consistent date formatting
nvidia['Date'] = pd.to_datetime(nvidia['Date']).dt.strftime('%Y-%m-%d')
bitcoin['Date'] = pd.to_datetime(bitcoin['Date']).dt.strftime('%Y-%m-%d')

# Select only relevant columns
nvidia = nvidia[['Date', 'Close']].rename(columns={'Close': 'NVDA_Close'})
bitcoin = bitcoin[['Date', 'Close']].rename(columns={'Close': 'BTC_Close'})

# Merge datasets by Date
merged_df = pd.merge(nvidia, bitcoin, on='Date', how='inner')

# Check merged data
print("\nMerged Data Preview:")
print(merged_df.head())

# Save merged data
merged_df.to_csv(merged_path, index=False)

print(f"\nMerged CSV successfully generated with {len(merged_df)} records at {merged_path}")
