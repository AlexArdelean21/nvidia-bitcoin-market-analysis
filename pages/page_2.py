import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from io import StringIO

st.title("Correlation & Regression Analysis")

# ---------------------- Restore DataFrame if needed ----------------------
if "df" not in st.session_state and "raw_csv" in st.session_state:
    st.session_state.df = pd.read_csv(StringIO(st.session_state.raw_csv))

if "df" in st.session_state:
    df = st.session_state.df

    st.subheader("Correlation Matrix")
    corr_matrix = df[['NVDA_Close', 'BTC_Close']].corr()
    st.write(corr_matrix)

    corr_value = corr_matrix.loc["NVDA_Close", "BTC_Close"]
    if abs(corr_value) > 0.8:
        interpretation = "There is a strong linear relationship between NVIDIA and Bitcoin prices."
    elif abs(corr_value) > 0.5:
        interpretation = "There is a moderate linear relationship between NVIDIA and Bitcoin prices."
    else:
        interpretation = "There is a weak or no linear relationship between NVIDIA and Bitcoin prices."

    st.info(f"Interpretation: {interpretation}")

    st.subheader("Scatter Plot with Regression Line")

    X = df[['NVDA_Close']]
    y = df['BTC_Close']
    X_with_const = sm.add_constant(X)
    model = sm.OLS(y, X_with_const).fit()
    predictions = model.predict(X_with_const)

    # Plotting
    fig, ax = plt.subplots()
    ax.scatter(df['NVDA_Close'], df['BTC_Close'], alpha=0.7, label='Actual')
    ax.plot(df['NVDA_Close'], predictions, color='red', label='Regression Line')
    ax.set_xlabel("NVIDIA Close Price")
    ax.set_ylabel("Bitcoin Close Price")
    ax.set_title("NVIDIA vs Bitcoin - Regression")
    ax.legend()
    st.pyplot(fig)

    st.caption("The red line shows the linear regression fit between NVIDIA and Bitcoin prices.")

    st.subheader("Multiple Linear Regression Summary")
    st.write(model.summary())

    st.info("Interpretation:\n"
            f"- **R-squared** of {model.rsquared:.3f} indicates that approximately {model.rsquared * 100:.2f}% "
            "of the variation in Bitcoin's price can be explained by NVIDIA's price.\n"
            f"- **P-value** of {model.pvalues[1]:.4f} for the NVDA_Close coefficient "
            f"{'is statistically significant' if model.pvalues[1] < 0.05 else 'is not statistically significant'}.")

    st.subheader("Residuals Plot")
    residuals = y - predictions
    fig2, ax2 = plt.subplots()
    ax2.scatter(predictions, residuals)
    ax2.axhline(0, color='red', linestyle='--')
    ax2.set_xlabel("Predicted BTC Price")
    ax2.set_ylabel("Residuals")
    ax2.set_title("Residuals vs Fitted")
    st.pyplot(fig2)
    st.caption("Residuals should be randomly scattered. Patterns may indicate poor model fit.")

else:
    st.warning("Please upload a merged CSV file on the Home page.")
