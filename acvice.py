import streamlit as st
from faker import Faker

# Instantiate the Faker object
fake = Faker()

# Streamlit app code
def generate_username_advice():
    st.title("Username Advice Generator")
    st.write("Get some username suggestions!")

    with st.form("username_form"):
        st.write("Enter your name:")
        name = st.text_input("Name")
        submit_button = st.form_submit_button("Generate")

    if submit_button:
        st.write("Username suggestions:")
        username = fake.user_name()
        st.write(username)

# Run the Streamlit app
if __name__ == "__main__":
    generate_username_advice()

