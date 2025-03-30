import yfinance as yf
import pandas as pd
import os

# Get Bitcoin historical data
bitcoin = yf.Ticker("BTC-USD")
bitcoin_data = bitcoin.history(start = "2023-03-26", end = "2025-03-26", interval = "1mo")
bitcoin_data.reset_index(inplace = True)

os.makedirs("data", exist_ok = True)
bitcoin_data.to_csv("./data/bitcoin_data.csv", index = False)

print("Bitcoin csv data succesfully generated in ../data/bitcoin_data.csv")

