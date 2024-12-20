import streamlit as st
import pandas as pd
from utils.s_functions import *

st.set_page_config(page_title="Stronghold Solutions", layout="wide")
st.title("Stronghold Solutions")

num_complete = 10
st.write(f"Completed Questions: **{str(num_complete)}**/105.")
st.progress(round(num_complete/105,2), text="Progress:")

tabs = st.tabs(["1-20", "21-40", "41-60","61-80","81-100","101-105"])

with tabs[0]:
    st.write("Questions 1 to 20:")

    #Q1
    with open("data/stronghold/rosalind_dna.txt","r") as f:
        q1text = f.read()
    with st.expander("See Q1 Solution"):
        st.write(q1(q1text))

    #Q2
    with open("data/stronghold/rosalind_rna.txt","r") as f:
        q2text = f.read()
    with st.expander("See Q2 Solution"):
        st.write(q2(q2text))

    #Q3
    with open("data/stronghold/rosalind_revc.txt","r") as f:
        q3text = f.read()
    with st.expander("See Q3 Solution"):
        st.write(q3(q3text))

    #Q4
    with st.expander("See Q4 Solution"):
        st.write(q4(5,3))
    #asked 29, 4; answer is 170361678269

    #Q5
    with st.expander("See Q5 Solution"):
        df = q5("data/stronghold/rosalind_gc.txt")
        df["GC-content"] = df["Sequence"].apply(q5_gcCalc)
        st.write(df)
        # Find the maximum GC-content
        max_gc_content = df["GC-content"].max()
        # Find the name associated with the maximum G-content
        max_gc_name = df[df["GC-content"] == max_gc_content]["Name"].values[0]
        st.write(f"Max GC-content Name: {max_gc_name}")
        st.write(f"GC-content Percentage: {max_gc_content}")

    #Q6
    with st.expander("See Q6 Solution"):
        st.write(q6("data/stronghold/rosalind_hamm.txt"))
    
    with st.expander("See Q7 Solution"):
        st.write(q7(18,22,25))
    
    with st.expander("See Q8 Solution"):
        st.write(q8("data/stronghold/rosalind_prot.txt"))
    
    with st.expander("See Q9 Solution"):
        st.write(q9("data/stronghold/rosalind_subs.txt"))

    with st.expander("See Q10 Solution"):
        df = q5("data/stronghold/rosalind_cons.txt")
        st.write(df)
        st.write(q10(df))

    with st.expander("See Q11 Solution"):
        st.write(q11(82,20))

    with st.expander("See Q12 Solution"):
        df = q5("data/stronghold/rosalind_grph.txt")
        output = q12(df,3)
        st.write("hello")
        st.write(output)

        # correct output already obtained, format to fit Rosalind answer
        s = ' '.join(map(str,output))
        s_clean = s.replace("(", "").replace(")", "").replace("'", "").replace(",", "")
        # Step 2: Split the string into words
        pairs = s_clean.split()

        # Step 3: Print pairs without commas
        for i in range(0, len(pairs), 2):
            print(pairs[i], pairs[i+1])
    
    with st.expander("See Q13 Solution"):
        # given: 18914 19552 17378 17497 18804 18236
        # sum the first 3 since they have same expected value of 2. 
        # ignore the last value since it has the expected value of 0
        # 17497 has expected value of 1.5, and 18804 has expected value of 1.
        # Multiply based on those expected values and sum them. 
        st.write(q13(55844,17497,18804))
    
    st.write("Q13")
    st.write("Q14")
    st.write("Q15")
    st.write("Q16")
    st.write("Q17")
    st.write("Q18")
    st.write("Q19")
    st.write("Q20")

