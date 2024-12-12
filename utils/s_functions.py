import pandas as pd

#q1 function 
def q1(s:str) -> list:
    return s.count("A"), s.count("G"), s.count("C"), s.count("T")

#q2 function
def q2(s:str) -> str:
    return s.replace("T","U")

#q3 function - reverse complement 
#nested replace with %temp% placeholders 
#https://www.geeksforgeeks.org/python-replace-multiple-characters-at-once/
def q3(s:str) -> str:
    reverse_s = s[::-1] #start:stop:step, no start/stop but step -1 reverses the string
    complement_s1 = reverse_s.replace('A', '%temp%').replace('T', 'A').replace('%temp%', 'T')
    complement_s2 = complement_s1.replace('C', '%temp%').replace('G', 'C').replace('%temp%', 'G')
    return complement_s2

#q4 function
#fib with variation - each adult pair will generate k pairs of rabbits
#how many pairs of rabbits exist after n generations?
#E.g. q4(5,3) : 1 -> 1 -> 4 -> 7 -> 19 
#Because 4 = 1(k) + 1; 7 = 1(k)+4; 19 = 4(k)+7
#Multiplier is applied on rabbit 2 generations ago. 
def q4(n:int,k:int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return q4(n-1, k) + k*q4(n-2, k)

#q5 function 
#GC-content in FASTA format
def q5(path:str):
    # Initialize empty lists to store sequence names and sequences
    names = []
    sequences = []
    # Open the FASTA file for reading
    with open(path, "r") as file:
        sequence = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):  # Header line
                if sequence:  # Save the previous sequence if it exists
                    sequences.append(sequence)
                    sequence = ""  # Reset for the new sequence
                names.append(line[1:])  # Store the name without the '>'
            else:
                sequence += line  # Append to the sequence
        if sequence:  # Add the last sequence
            sequences.append(sequence)

    # Create a DataFrame from the parsed data
    df = pd.DataFrame({
        "Name": names,
        "Sequence": sequences
    })
    return df

def q5_gcCalc(s:str):
    return ((s.count("G") + s.count("C")) / len(s)) * 100