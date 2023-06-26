import os
import streamlit as st

# Get the username
username = os.getenv("USER")

# Display the username in your Streamlit app
st.write(f"Username: {username}")
