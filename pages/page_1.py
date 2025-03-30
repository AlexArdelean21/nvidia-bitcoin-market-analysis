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

st.markdown("""
<h2 style='color:#ff5733;'>\U0001F4CA Statistical Analysis of NVIDIA & Bitcoin</h2>
<p style='color:gray;'>This section explores missing values, volatility, outliers, and distribution using visual and statistical tools.</p>
""", unsafe_allow_html=True)

st.subheader("\U0001F5C3️ Raw Data Preview")
st.dataframe(df.head(), use_container_width=True)
st.caption("Preview of the first few records in the merged dataset.")

st.subheader("\U0001F50D Handling Missing Values")
missing_before = df.isnull().sum()
st.write("Missing values before handling:", missing_before)

if missing_before.sum() == 0:
    st.success("No missing values detected. ✅")
else:
    df.fillna(df.mean(numeric_only=True), inplace=True)
    missing_after = df.isnull().sum()
    st.write("Missing values after handling:", missing_after)
    st.info("Missing values filled using mean imputation.")

st.subheader("\U0001F4C8 Descriptive Statistics")
df_numeric = df.select_dtypes(include=[np.number])
st.write(df_numeric.describe())

st.subheader("\U0001F4A1 Detecting Extreme Values")
z_scores = np.abs((df_numeric - df_numeric.mean()) / df_numeric.std())
extreme_values = (z_scores > 3).sum()
st.write("Extreme Values (z-score > 3):", extreme_values)

with st.expander("📦 Boxplot for Outlier Detection"):
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    ax[0].boxplot(df['NVDA_Close'])
    ax[0].set_title('NVIDIA Close Prices')
    ax[1].boxplot(df['BTC_Close'])
    ax[1].set_title('Bitcoin Close Prices')
    st.pyplot(fig)

st.subheader("\U0001F311 Volatility (Standard Deviation)")
volatility = df_numeric.std()
st.write(volatility)

st.subheader("\U0001F4C6 Rolling Averages (3-month window)")
df['NVDA_Rolling'] = df['NVDA_Close'].rolling(window=3).mean()
df['BTC_Rolling'] = df['BTC_Close'].rolling(window=3).mean()

col1, col2 = st.columns(2)
with col1:
    st.line_chart(df[['NVDA_Close', 'NVDA_Rolling']])
    st.caption("NVIDIA Trend")
with col2:
    st.line_chart(df[['BTC_Close', 'BTC_Rolling']])
    st.caption("Bitcoin Trend")

st.subheader("\U0001F3A8 Scaled Data")
scaler = MinMaxScaler()
scaled_data = pd.DataFrame(scaler.fit_transform(df_numeric), columns=df_numeric.columns)
st.dataframe(scaled_data.head(), use_container_width=True)

st.subheader("\U0001F4D0 Histograms of Scaled Data")
fig_hist = scaled_data.hist(figsize=(10, 8))
st.pyplot(plt)

st.subheader("📉 Kurtosis & Skewness (scaled)")
st.write("Kurtosis:", scaled_data.kurtosis())
st.write("Skewness:", scaled_data.skew())

st.subheader("\U0001F4CA Correlation Heatmap")
fig, ax = plt.subplots()
sns.heatmap(df_numeric.corr(), annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

st.success("✅ Statistical analysis complete. Explore correlation and regression in the next tab.")