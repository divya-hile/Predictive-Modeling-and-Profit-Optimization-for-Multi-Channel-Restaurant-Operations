import streamlit as st
import pandas as pd

st.set_page_config(page_title="Restaurant Profit Optimization", layout="centered")

st.title("🍽️ Restaurant Profit Optimization")
st.write(
    """
    This app demonstrates predictive modeling and profit optimization
    for multi-channel restaurant operations.
    """
)

st.subheader("Project Overview")
st.write("""
- Predict monthly profit using synthetic restaurant data  
- Analyze impact of delivery commission rates  
- Support data-driven decision making
""")

st.subheader("Sample Output")
data = {
    "Commission Rate (%)": [10, 20, 30],
    "Predicted Profit (₹)": [120000, 85000, 50000]
}
df = pd.DataFrame(data)
st.table(df)

st.success("This Streamlit app is successfully deployed 🎉")

