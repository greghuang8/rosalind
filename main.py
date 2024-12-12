import streamlit as st
import pandas as pd

# Create an interactive streamlit page to show my solutions to Rosalind questions.
# Set up main landing page
st.set_page_config(page_title="Rosalind Solutions", layout="wide")
st.title("Rosalind Bioinformatics Project")

with open('README.md', 'r') as file:
    markdown_text = file.read()
st.markdown(markdown_text)