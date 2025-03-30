import yfinance as yf
import pandas as pd
import os

# Get NVIDIA historical data
nvidia = yf.Ticker("NVDA")
nvidia_data = nvidia.history(start = "2023-03-26", end = "2025-03-26", interval = "1mo")
nvidia_data.reset_index(inplace = True)

os.makedirs("data", exist_ok = True)
nvidia_data .to_csv("./data/nvidia_data.csv", index = False)

print("NVIDIA csv data succesfully generated in ../data/nvidia_data.csv")
