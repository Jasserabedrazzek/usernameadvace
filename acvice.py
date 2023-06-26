import socket
import streamlit as st

def get_hostname_advice():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    advice = f"Hostname: {hostname}\nIP Address: {ip_address}"
    return advice

# Streamlit app code
st.title("Hostname Advice")
advice = get_hostname_advice()
st.text(advice)
