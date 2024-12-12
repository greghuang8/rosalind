import streamlit as st
import pandas as pd

st.set_page_config(page_title="Stronghold Solutions", layout="wide")
st.title("Stronghold Solutions")

num_complete = 0
st.write(f"Completed Questions: **{str(num_complete)}**/105.")
st.progress(round(num_complete/105,1), text="Progress:")

tabs = st.tabs(["1-20", "21-40", "41-60","61-80","81-100","101-105"])

with tabs[0]:
    st.write("Questions 1 to 20:")
    st.write("Q1")
    st.write("Q2")
    st.write("Q3")
    st.write("Q4")
    st.write("Q5")
    st.write("Q6")
    st.write("Q7")
    st.write("Q8")
    st.write("Q9")
    st.write("Q10")
    st.write("Q11")
    st.write("Q12")
    st.write("Q13")
    st.write("Q14")
    st.write("Q15")
    st.write("Q16")
    st.write("Q17")
    st.write("Q18")
    st.write("Q19")
    st.write("Q20")

