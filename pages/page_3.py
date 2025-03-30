import streamlit as st
import pandas as pd
from io import StringIO

st.markdown("""
<h2 style='color:#ff5733;'>🤔 Conclusion & Insights</h2>
<p style='color:gray;'>Summarizing analytical findings and drawing economic interpretations based on our NVIDIA-Bitcoin study.</p>
""", unsafe_allow_html=True)

# Restore data if needed
if "df" not in st.session_state and "raw_csv" in st.session_state:
    st.session_state.df = pd.read_csv(StringIO(st.session_state.raw_csv))

if "df" in st.session_state:
    df = st.session_state.df

    st.header("🔄 Key Insights Summary")

    st.markdown("""
    - 🔢 **Correlation Coefficient** between NVIDIA and Bitcoin prices shows the **strength of linear relationship**.
    - 📊 **Regression analysis** suggests that fluctuations in NVIDIA's stock price may **partially explain movements in Bitcoin**.
    - 📈 **R-squared** value quantifies how much variance in Bitcoin prices is explained by NVIDIA — not causation, but indication.
    - 🔍 **Residual patterns** help assess model fit; ideally, they should be randomly scattered.
    - 📉 **Volatility analysis** reveals **Bitcoin tends to be more volatile** than NVIDIA.
    """)

    st.divider()

    st.header("🌐 Economic Interpretation")

    st.markdown("""
    - There is **some degree of synchronization** between tech market dynamics (e.g., NVIDIA's performance) and the crypto market.
    - This might be attributed to shared investor sentiment, speculative trends, or macroeconomic factors.
    - While correlation and regression exist, **NVIDIA is not a strong predictor** of Bitcoin price by itself.
    - Investors should treat such relationships as **insights**, not predictions.
    """)

    st.success("\u2705 Analysis completed. Use the navigation bar to explore specific sections again.")

else:
    st.warning("Please upload the merged CSV file from the Home page.")
