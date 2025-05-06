import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load and clean the data
df = pd.read_csv('IFA.csv')
df = df.drop("Unnamed: 0", axis=1)
df['Date'] = pd.to_datetime(df['Date'])

# Set the page title
st.title("Stock Closing Price Viewer")

# Display available stock symbols
symbols = df['Symbol'].unique()
selected_symbol = st.selectbox("Select a stock symbol:", symbols)

# Filter data for the selected stock
stk = df[df['Symbol'] == selected_symbol]

# Plotting
st.subheader(f"Closing Prices for {selected_symbol}")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=stk['Date'], y=stk['Close'], ax=ax)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)
