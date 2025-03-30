import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from io import StringIO

st.markdown("""
<h2 style='color:#ff5733;'>✨ Correlation & Regression Analysis</h2>
<p style='color:gray;'>Explore the relationship between NVIDIA and Bitcoin prices using correlation and linear regression models.</p>
""", unsafe_allow_html=True)

# ---------------------- Restore DataFrame if needed ----------------------
if "df" not in st.session_state and "raw_csv" in st.session_state:
    st.session_state.df = pd.read_csv(StringIO(st.session_state.raw_csv))

if "df" in st.session_state:
    df = st.session_state.df

    st.subheader("🔄 Correlation Matrix")
    corr_matrix = df[['NVDA_Close', 'BTC_Close']].corr()
    st.dataframe(corr_matrix, use_container_width=True)

    corr_value = corr_matrix.loc["NVDA_Close", "BTC_Close"]
    if abs(corr_value) > 0.8:
        interpretation = "Strong linear relationship"
    elif abs(corr_value) > 0.5:
        interpretation = "Moderate linear relationship"
    else:
        interpretation = "Weak or no linear relationship"

    st.info(f"Interpretation: {interpretation} ({corr_value:.2f})")

    st.subheader("🔺 Scatter Plot with Regression Line")

    X = df[['NVDA_Close']]
    y = df['BTC_Close']
    X_with_const = sm.add_constant(X)
    model = sm.OLS(y, X_with_const).fit()
    predictions = model.predict(X_with_const)

    fig, ax = plt.subplots()
    ax.scatter(df['NVDA_Close'], df['BTC_Close'], alpha=0.7, label='Actual')
    ax.plot(df['NVDA_Close'], predictions, color='red', label='Regression Line')
    ax.set_xlabel("NVIDIA Close Price")
    ax.set_ylabel("Bitcoin Close Price")
    ax.set_title("NVIDIA vs Bitcoin - Regression")
    ax.legend()
    st.pyplot(fig)
    st.caption("The red line shows the linear regression fit between NVIDIA and Bitcoin prices.")

    st.subheader("📊 Multiple Linear Regression Summary")
    st.write(model.summary())

    st.info("Interpretation:\n"
            f"- **R-squared**: {model.rsquared:.3f} (~{model.rsquared * 100:.2f}% variance explained)\n"
            f"- **P-value** for NVDA_Close: {model.pvalues[1]:.4f} → "
            f"{'statistically significant ✅' if model.pvalues[1] < 0.05 else 'not statistically significant ❌'}")

    st.subheader("🌎 Residuals Plot")
    residuals = y - predictions
    fig2, ax2 = plt.subplots()
    ax2.scatter(predictions, residuals)
    ax2.axhline(0, color='red', linestyle='--')
    ax2.set_xlabel("Predicted BTC Price")
    ax2.set_ylabel("Residuals")
    ax2.set_title("Residuals vs Fitted")
    st.pyplot(fig2)
    st.caption("Residuals should be randomly scattered. Patterns may indicate poor model fit.")

    st.success("✅ Regression analysis complete. Proceed to the insights tab for conclusions.")

else:
    st.warning("Please upload a merged CSV file on the Home page.")
