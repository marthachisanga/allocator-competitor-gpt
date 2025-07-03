import streamlit as st
import pandas as pd

# Load the Excel file
df = pd.read_excel("gpt.xlsx", sheet_name="Sheet2")

st.title("Allocator Competitor Lookup Tool")
st.write("Search internal notes about competitors to assist during SDR calls.")

# Input box
query = st.text_input("🔍 Enter Competitor Name").strip().lower()

# Search logic
if query:
    results = df[df['Competitor Name'].str.lower().str.contains(query, na=False)]
    
    if not results.empty:
        for _, row in results.iterrows():
            st.subheader(row['Competitor Name'].title())
            st.write(row['Internal Notes'])
    else:
        st.warning("No matching competitor found.")
else:
    st.info("Type a competitor name above to begin searching.")
