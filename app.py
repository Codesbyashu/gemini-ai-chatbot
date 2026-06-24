import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Streamlit UI
st.set_page_config(
    page_title="Gemini ChatBot",
    page_icon="🤖",
    layout="wide"
)

st.header("🤖 Gemini ChatBot")

user_input = st.text_input("Enter your query here")

if st.button("Submit"):

    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        try:
            response = model.generate_content(user_input)
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")