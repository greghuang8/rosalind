import streamlit as st

st.set_page_config(page_title="Heights Solutions", layout="wide")
st.title("Heights Solutions")

num_complete = 0
st.write(f"Completed Questions: **{str(num_complete)}**/34.")
st.progress(round(num_complete/34,1), text="Progress: ")
tabs = st.tabs(["1-10", "11-20","21-30","31-34"])

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
    st.write("Questions 11 to 20:")
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

with tabs[2]:
    st.write("Questions 21 to 30:")
    st.write("Q21")
    st.write("Q22")
    st.write("Q23")
    st.write("Q24")
    st.write("Q25")
    st.write("Q26")
    st.write("Q27")
    st.write("Q28")
    st.write("Q29")
    st.write("Q30")

with tabs[3]:
    st.write("Questions 31 to 34:")
    st.write("Q31")
    st.write("Q32")
    st.write("Q33")
    st.write("Q34")