import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from io import StringIO

# 🔐 Check and load CSV data
if "df" not in st.session_state:
    if "raw_csv" in st.session_state:
        try:
            df = pd.read_csv(StringIO(st.session_state.raw_csv))
            st.session_state.df = df
        except Exception as e:
            st.error(f"❌ Error loading CSV data: {e}")
            st.stop()
    else:
        st.error("❗ No CSV file found. Please upload one on the Home page.")
        st.stop()

# ✅ At this point, df is guaranteed to exist and be valid
df = st.session_state.df

st.title("Statistical Analysis of NVIDIA & Bitcoin")

if "df" in st.session_state:
    df = st.session_state.df

    st.subheader("Raw Data")
    st.write(df.head())
    st.caption("Preview of the first few records in the merged dataset.")

    st.subheader("Handling Missing Values")
    missing_before = df.isnull().sum()
    st.write("Missing values before handling:\n", missing_before)

    if missing_before.sum() == 0:
        st.info("No missing values detected. No imputation needed.")
    else:
        df.fillna(df.mean(numeric_only=True), inplace=True)
        missing_after = df.isnull().sum()
        st.write("Missing values after handling:\n", missing_after)
    st.caption("Missing values are checked and filled using mean imputation if present.")

    st.subheader("Descriptive Statistics")
    df_numeric = df.select_dtypes(include=[np.number])
    st.write(df_numeric.describe())
    st.caption("Summarizes central tendency, spread, and range of the dataset.")

    st.subheader("Detecting Extreme Values")
    z_scores = np.abs((df_numeric - df_numeric.mean()) / df_numeric.std())
    extreme_values = (z_scores > 3).sum()
    st.write("Extreme Values (z-score > 3):")
    st.write(extreme_values)
    st.caption("Values with z-scores greater than 3 are considered statistical outliers.")

    st.subheader("Boxplot for Outlier Detection")
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    ax[0].boxplot(df['NVDA_Close'])
    ax[0].set_title('NVIDIA Close Prices')
    ax[1].boxplot(df['BTC_Close'])
    ax[1].set_title('Bitcoin Close Prices')
    st.pyplot(fig)
    st.caption("Boxplots show data distribution and highlight any potential outliers visually.")

    st.subheader("Volatility (Standard Deviation)")
    volatility = df_numeric.std()
    st.write(volatility)
    st.caption("Higher standard deviation indicates more price fluctuation or volatility.")

    st.subheader("Rolling Averages (3-month window)")
    df['NVDA_Rolling'] = df['NVDA_Close'].rolling(window=3).mean()
    df['BTC_Rolling'] = df['BTC_Close'].rolling(window=3).mean()

    st.line_chart(df[['NVDA_Close', 'NVDA_Rolling']])
    st.line_chart(df[['BTC_Close', 'BTC_Rolling']])
    st.caption("Rolling averages smooth short-term fluctuations to highlight trends.")

    st.subheader("Scaled Data")
    scaler = MinMaxScaler()
    scaled_data = pd.DataFrame(scaler.fit_transform(df_numeric), columns=df_numeric.columns)
    st.write(scaled_data.head())
    st.caption("Min-Max Scaling transforms features to a range between 0 and 1.")

    st.subheader("Histograms of Scaled Data")
    scaled_data.hist(figsize=(10, 8))
    st.pyplot(plt)
    st.caption("Histograms show the distribution of the scaled features.")

    st.subheader("Kurtosis & Skewness (scaled)")
    st.write("Kurtosis:\n", scaled_data.kurtosis())
    st.write("Skewness:\n", scaled_data.skew())
    st.caption("Kurtosis measures tailedness, skewness shows asymmetry of the distribution.")

    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(df_numeric.corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)
    st.caption("Displays pairwise correlation between numeric features.")

else:
    st.warning("Please upload a merged CSV file on the Home page.")
