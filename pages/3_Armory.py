import streamlit as st

st.set_page_config(page_title="Armory Solutions", layout="wide")
st.title("Armory Solutions")

num_complete = 0
st.write(f"Completed Questions: **{str(num_complete)}**/15.")
st.progress(round(num_complete/15,1), text="Progress:")

tabs = st.tabs(["1-10", "11-15"])
with tabs[0]:
    st.write("Questions 1 to 10:")
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

with tabs[1]:
    st.write("Questions 11 to 15:")
    st.write("Q11")
    st.write("Q12")
    st.write("Q13")
    st.write("Q14")
    st.write("Q15")
