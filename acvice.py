import socket
import getpass
import streamlit as st

# Get the hostname and username
hostname = socket.gethostname()
username = getpass.getuser()

# Display the hostname and username in your Streamlit app
st.write(f"Hostname: {hostname}")
st.write(f"Username: {username}")
