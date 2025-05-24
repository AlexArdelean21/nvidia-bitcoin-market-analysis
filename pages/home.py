import streamlit as st
import pandas as pd
from io import StringIO

# ------------------------ Navigation Logic ------------------------
params = st.query_params
if "page" not in st.session_state and "page" in params:
    st.session_state.page = params["page"]

def navigate_to(page_name):
    st.session_state.page = page_name
    st.query_params["page"] = page_name


# ------------------------ Styling ------------------------
st.markdown("""
    <style>
    .cool-button {
        position: relative;
        display: inline-block;
        padding: 12px 28px;
        font-size: 16px;
        font-weight: bold;
        color: #ff5733;
        border: 2px solid #ff5733;
        background: transparent;
        border-radius: 12px;
        overflow: hidden;
        cursor: pointer;
        transition: color 0.4s ease-in-out;
        margin-bottom: 15px;
        width: 100%;
        text-align: center;
    }

    .cool-button::before {
        content: "";
        position: absolute;
        top: 100%;
        left: 100%;
        width: 200px;
        height: 150px;
        background: #ff5733;
        transition: all 0.6s ease-in-out;
        z-index: -1;
        transform: rotate(45deg);
    }

    .cool-button:hover {
        color: white;
    }

    .cool-button:hover::before {
        top: -30px;
        left: -30px;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------------ Sidebar Navigation ------------------------
st.sidebar.markdown("### 📁 Navigation")

if st.sidebar.button("📈 Statistical Analysis"):
    navigate_to("page_1")

if st.sidebar.button("📊 Correlation & Regression"):
    navigate_to("page_2")

if st.sidebar.button("🧠 Conclusion & Insights"):
    navigate_to("page_3")
    
if st.sidebar.button("Surprise"):
    navigate_to("extra_page")  # or "page_jumpscare" if renamed


# Apply CSS to Streamlit buttons AFTER render
st.sidebar.markdown("""
    <script>
        const buttons = window.parent.document.querySelectorAll('section[data-testid="stSidebar"] button');
        buttons.forEach(btn => btn.classList.add("cool-button"));
    </script>
""", unsafe_allow_html=True)

# ------------------------ Main Header ------------------------
st.markdown("<h1 style='text-align: center; color: #ff5733;'>NVIDIA & Bitcoin Market Analysis</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Upload your merged CSV file to begin exploring the data.</p>", unsafe_allow_html=True)

# ------------------------ File Upload ------------------------
uploaded_file = st.file_uploader("Upload merged CSV file", type=["csv"])

if uploaded_file is not None:
    raw_csv = uploaded_file.getvalue().decode("utf-8")
    st.session_state.raw_csv = raw_csv
    st.session_state.df = pd.read_csv(StringIO(raw_csv))
    st.success("✅ File uploaded successfully!")

elif "raw_csv" in st.session_state and "df" not in st.session_state:
    st.session_state.df = pd.read_csv(StringIO(st.session_state.raw_csv))

# ------------------------ Load Active Page ------------------------
if "page" in st.session_state:
    if st.session_state.page == "page_1":
        with open("pages/page_1.py", encoding="utf-8") as file:
            code = compile(file.read(), "page_1.py", "exec")
            exec(code, {"st": st, "pd": pd, "plt": __import__("matplotlib.pyplot"),
                        "np": __import__("numpy"), "sns": __import__("seaborn"),
                        "sm": __import__("statsmodels.api"), "StringIO": StringIO})
    elif st.session_state.page == "page_2":
        with open("pages/page_2.py", encoding="utf-8") as file:
            code = compile(file.read(), "page_2.py", "exec")
            exec(code, {"st": st, "pd": pd, "plt": __import__("matplotlib.pyplot"),
                        "sm": __import__("statsmodels.api"), "StringIO": StringIO})
    elif st.session_state.page == "page_3":
        with open("pages/page_3.py", encoding="utf-8") as file:
            code = compile(file.read(), "page_3.py", "exec")
            exec(code, {"st": st, "pd": pd, "StringIO": StringIO})

    elif st.session_state.page == "extra_page":  # or "page_jumpscare"
        with open("pages/extra_page.py", encoding="utf-8") as file:
            code = compile(file.read(), "extra_page.py", "exec")
            exec(code, {"st": st, "time": __import__("time")})
