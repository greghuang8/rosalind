import pandas as pd
import itertools as it

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
# helper function to get GC-content in the DF
def q5_gcCalc(s:str):
    return ((s.count("G") + s.count("C")) / len(s)) * 100


def q6(path:str):
    with open (path,'r') as file:
        first = ""
        for line in file:
            if first == "":
                first = line
            else:
                second = line
    #Basic solution
    counter = 0
    for i,char in enumerate(first):
        if second[i] != char:
            counter+=1

    #OR 
    counter = sum(a != b for a, b in zip(first, second))
    return counter

def q7(k,m,n):
    total = k+m+n
    total2 = total-1
    #remove situations with both recessive by counting cases
    # case of probability WITHOUT replacement
    return 1 - (m/total*(m-1)/(total2)*0.25) - (m/total * n/total2*0.5) - (n/total*m/total2*0.5) - (n/total*(n-1)/total2)

def q8(path:str):
    translate_table = """UUU F      CUU L      AUU I      GUU V
                UUC F      CUC L      AUC I      GUC V
                UUA L      CUA L      AUA I      GUA V
                UUG L      CUG L      AUG M      GUG V
                UCU S      CCU P      ACU T      GCU A
                UCC S      CCC P      ACC T      GCC A
                UCA S      CCA P      ACA T      GCA A
                UCG S      CCG P      ACG T      GCG A
                UAU Y      CAU H      AAU N      GAU D
                UAC Y      CAC H      AAC N      GAC D
                UAA Stop   CAA Q      AAA K      GAA E
                UAG Stop   CAG Q      AAG K      GAG E
                UGU C      CGU R      AGU S      GGU G
                UGC C      CGC R      AGC S      GGC G
                UGA Stop   CGA R      AGA R      GGA G
                UGG W      CGG R      AGG R      GGG G"""
    
    with open(path,'r') as file:
        mrna = file.read()
    
    prot = ""
    translate_list = translate_table.split()
    translate_dict = dict(zip(translate_list[0::2],translate_list[1::2]))
    for i in range(0, len(mrna)-3, 3):
        prot += translate_dict[mrna[i:i+3]]
    return prot

def q9(path:str):
    with open(path,'r') as file:
        sequence = ""
        for line in file:
            line=line.strip() # remove '\n'
            if sequence == "":
                sequence = line
            else:
                motif = line
    indices = []
    for i in range(0, len(sequence)-len(motif)):
        if sequence[i:i+len(motif)]==motif:
            indices.append(i)
    return indices, sequence, motif

def q10(df:pd.DataFrame):
    consensus_dict = {"A":"", "C":"","G":"","T":""}
    consensus_string = ""
    for index in range(0, len(df['Sequence'][0])):
        a_count = 0
        c_count = 0
        g_count = 0
        t_count = 0
        for item in df['Sequence']:
            if item[index] == 'A':
                a_count += 1
            elif item[index] == 'C':
                c_count += 1
            elif item[index] == "G":
                g_count += 1
            elif item[index] == "T":
                t_count += 1
        maximum = max(a_count,c_count,g_count,t_count)
        tiebreak = 0
        if maximum == a_count and tiebreak ==0:
            consensus_string += 'A'
            tiebreak +=1
        elif maximum == c_count and tiebreak ==0:
            consensus_string += 'C'
            tiebreak+=1
        elif maximum == g_count and tiebreak ==0:
            consensus_string += 'G'
            tiebreak+=1
        elif maximum == t_count and tiebreak ==0:
            consensus_string += 'T'
            tiebreak+=1

        consensus_dict["A"] += (str(a_count) + " ")
        consensus_dict["C"] += (str(c_count) + " ")
        consensus_dict["G"] += (str(g_count) + " ")
        consensus_dict["T"] += (str(t_count) + " ")
    return  consensus_string, consensus_dict

#Fib w/ dead rabbits
#https://saradoesbioinformatics.blogspot.com/2016/06/mortal-fibonacci-rabbits.html
def q11(n:int, m:int):
    rabbits_seq = [1,1]
    months = 2
    offset = m + 1
    while months < n:
        if months < m:
            rabbits_seq.append(rabbits_seq[-2]+rabbits_seq[-1])
        elif months == m:
            rabbits_seq.append(rabbits_seq[-2]+rabbits_seq[-1]-1)
        else: 
            rabbits_seq.append(rabbits_seq[-2]+rabbits_seq[-1]-rabbits_seq[-offset])
        months += 1
    return rabbits_seq[-1]

#Graph problem 
# In this example, the overlap graph is O3, where the first 3 and the last 3 bp need to match
# https://stackoverflow.com/questions/27878067/rosalind-overlap-graphs
def q12(df:pd.DataFrame,k:int):
    #convert input df to dict
    dna_map = df.set_index('Name')['Sequence'].to_dict()
    
    # set empty output list 
    edges = []
    #using itertools.combinations, get the pairs of names in the dna_map dictionary
    name_pairs = it.combinations(dna_map, 2)
    
    #iterate through each pair of names, u = first name, v = second name in pair
    # and then get the corresponding sequence
    for u,v in name_pairs:
        u_dna, v_dna = dna_map[u], dna_map[v] #get the sequences associated to name from dictionary
        if u_dna[-k:] == v_dna[:k]:
            edges.append((u,v))
        if v_dna[-k:] == u_dna[:k]:
            edges.append((v,u))
    
    return edges

def q13(a,b,c):
    return a*2+b*1.5+c
