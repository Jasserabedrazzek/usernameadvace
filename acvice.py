import streamlit as st
import requests

def get_username_advice():
    st.title("GitHub Username Advice")
    username = st.text_input("Enter GitHub username:")
    
    if st.button("Get Advice"):
        # Call the GitHub API
        response = requests.get(f"https://api.github.com/users/{username}")
        
        if response.status_code == 200:
            data = response.json()
            advice = data.get("bio", "No advice available")
            st.success(f"Advice for {username}: {advice}")
        else:
            st.error("Unable to fetch data. Please check the username.")

if __name__ == "__main__":
    get_username_advice()
