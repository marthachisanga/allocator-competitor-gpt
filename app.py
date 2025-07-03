import streamlit as st
import pandas as pd
from PIL import Image

# --- Logo ---
logo = Image.open("allocator-logo.png")  # Replace with your file name
st.image(logo, width=180)

st.title("Allocator Competitor Lookup Tool")
st.write("🔍 Search internal notes about competitors to assist during SDR calls.")

# Load Excel
df = pd.read_excel("gpt.xlsx", sheet_name="Sheet2")

# Search input
query = st.text_input("Enter Competitor Name").strip().lower()

if query:
    results = df[df['Competitor Name'].str.lower().str.contains(query, na=False)]
    
    if not results.empty:
        for _, row in results.iterrows():
            st.subheader(row['Competitor Name'].title())
            notes = str(row['Internal Notes'])

            # Bullet point formatting
            bullets = [note.strip() for note in notes.split('.') if note.strip()]
            for bullet in bullets:
                st.markdown(f"- {bullet}")
    else:
        st.warning("No matching competitor found.")
else:
    st.info("Type a competitor name above to begin searching.")
