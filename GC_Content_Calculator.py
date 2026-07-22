from Bio import SeqIO
record = SeqIO.read("sequence.fasta", "fasta")
sequence = str(record.seq)
print(record.id)
print(record.description)
print(record.seq)
print(len(sequence))


def percentage_GC(sequence): #Defining a function in python
    total_bases = len(sequence) #Finding the length of the sequence
    
    GC_content = sequence.count("G")+ sequence.count("C") #Finding the number of G's and C's in the sequence and adding them together
   
    percentage_GC = (GC_content/total_bases)*100 #Calculating the percentage of GC 
    
    GC_rounded = round(percentage_GC,2) #Rounding off the answer
    return(GC_rounded)

print(percentage_GC(sequence), "%")



