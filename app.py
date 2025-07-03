import streamlit as st
import pandas as pd

# --- Display Allocator Logo ---
st.image("https://www.allocator.com/hubfs/post_feat-img_default.png", width=180)

st.title("Allocator Competitor Lookup")
st.write("🔍 Quickfire notes about competitors to assist during outreach calls.")

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

            # Format internal notes into bullet points
            bullets = [note.strip() for note in notes.replace('\n', '.').split('.') if note.strip()]
            for bullet in bullets:
                st.markdown(f"- {bullet}")
    else:
        st.warning("No matching competitor found.")
else:
    st.info("Type a competitor name above to begin searching.")
