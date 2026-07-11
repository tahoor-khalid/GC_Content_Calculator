def percentage_GC(sequence): #Defining a function in python
    bases = sequence
    total_bases = len(bases) #Finding the length of the sequence
    
    GC_content = bases.count("G")+bases.count("C") #Finding the number of G's and C's in the sequence and adding them together
   
    percentage_GC = (GC_content/total_bases)*100 #Calculating the percentage of GC 
    
    GC_rounded = round(percentage_GC,2) #Rounding off the answer
    return(GC_rounded)

sequence = "ATCTGTCGTACGTCAGT"
print(sequence)
print(percentage_GC(sequence), "%")
