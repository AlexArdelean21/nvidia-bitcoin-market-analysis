
# 📊 NVIDIA & Bitcoin Market Analysis

This Streamlit dashboard explores the potential correlation between **NVIDIA's stock prices (NVDA)** and **Bitcoin (BTC)** over time. It includes financial data analysis, regression modeling, and insightful visualizations.

---

## 🗂️ Project Structure

```
├── data/
│   ├── bitcoin_data.csv        # Raw Bitcoin data
│   ├── merged_data.csv         # Merged NVDA + BTC data
│   └── nvidia_data.csv         # Raw NVIDIA data
│
├── pages/
│   ├── home.py                 # Main dashboard and navigation
│   ├── page_1.py               # Statistical analysis (descriptive stats, outliers, scaling)
│   ├── page_2.py               # Correlation & regression analysis
│   └── page_3.py               # Conclusion & insights
│
├── scripts/
│   ├── get_bitcoin_data.py     # Downloads Bitcoin data using yfinance
│   ├── get_data.py             # Downloads NVIDIA data using yfinance
│   └── merge_data.py           # Merges both datasets on Date
│
├── .gitignore
├── requirements.txt            # Python dependencies
├── run_streamlit.bat           # Quick launcher (for Windows)
└── venv/                       # (optional) Python virtual environment
```

---

## 🚀 How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/nvidia-bitcoin-market-analysis.git
   cd nvidia-bitcoin-market-analysis
   ```

2. **Create virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   venv\Scripts\activate     # On Windows
   source venv/bin/activate  # On Mac/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   streamlit run pages/home.py
   ```

   Or use the included shortcut for Windows:
   ```bash
   run_streamlit.bat
   ```

---

## 📌 Key Features

- 📈 **Statistical Analysis** – missing values, extreme values, descriptive stats
- 📉 **Volatility & Rolling Averages** – visualize short- and long-term trends
- 📐 **Correlation & Regression** – determine if NVDA stock predicts BTC movement
- 📊 **Interactive Charts & Heatmaps** – powered by `matplotlib` and `seaborn`
- 🧠 **Conclusion Page** – business interpretation of analysis results

---

## 🛠️ Tech Stack

- **Python 3.10+**
- [Streamlit](https://streamlit.io/)
- [pandas](https://pandas.pydata.org/)
- [yfinance](https://pypi.org/project/yfinance/)
- [matplotlib](https://matplotlib.org/)
- [seaborn](https://seaborn.pydata.org/)
- [scikit-learn](https://scikit-learn.org/)
- [statsmodels](https://www.statsmodels.org/)

---


*Developed for the Software Packages Seminar – CSIE Faculty, Year 3.*
