#Myra Ribeiro
#2022/12/21
#the purpose of this program is to take a dna text file input, print its rna then print the proteins normally, at an offset of one, and at an offset of two.
print("hello and welcome to my program! this program takes a dna text file and prints its rna, then prints the proteins at an offset of one, normally, and at an offset of two.")
#hello statement
print(" ")

print("Lets start with a joke, shall we? Why did the bacteria cross the microscope?") #funny joke

print(" ")

print("To get to the other slide!!! Anyways continuing... (please note that any * output results in the following dna or rna or protein sequences are the equivalent of a STOP codon.")
print(" ")#funny joke ending - any * in the programm  = 'stop' codon sequence

test = open('DNAasSampleRun.txt', "r")#import the test file
dna = (str(test.readlines()))#turn it into a string
dna = dna[2:-2]#the test file imports with ['string'] so this is a way of removing characters by using string manipulation.

#this removes any chars that could potentially affect code processing. text not included.
dna = dna.replace('[', '')#removes any [ in the text
dna = dna.replace(']', '')#removes any ] in the text
dna = dna.replace(',','')#removes any ',' in the text
dna = dna.replace("'", '')#removes any ' in the text
dna = dna.replace(" ", '')#removes any space in the text
dna = dna.replace('""', '')#removes any " in the text
dna = dna.replace('\\', '')#removes backslashes in the test
dna = dna.replace('n', '')#removes n in the text

print("Your DNA is...", dna) #print dna

rna = '' #rna empty string (to hold rna)

for i in dna: #translate dna to rna
    if i == "A":
        rna = rna + "U" #assigns u to rna where a would have been... this repeats for c, g, and t as well.
    elif i == "C":
        rna = rna + "G"
    elif i == "G":
        rna = rna + "C"
    elif i == "T":
        rna = rna + "A"

print("your RNA is (according to transcription)... ", rna) #output rna to user

new_rna = '' #initalize new rna list - to convert into rna the other specified way

for i in dna:#translate dna to rna
    if i == "T":
        new_rna = new_rna+"U" #assigns u to rna where t would have been
    elif i == "C":
        new_rna = new_rna + "C" #same process with t and u ... this repeats for G and A as well
    elif i == "G":
        new_rna = new_rna+"G"
    elif i == "A":
        new_rna = new_rna + "A"

print("your RNA is (when switching t and u)...", new_rna) #print new rna to user
        

def translate(dna): #define function to translate dna into protiens (no offset)
    codon_table = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
} #initalize table of codons
    
    proteins = [] #initalize empty list
    
    if int(len(dna) % 3) == 0: #this assures that it is divisible by three. if not divisible by three, then the program removes the final chars (this is assuming its divisible by three)
        
        for i in range(0, len(dna), 3): #this for loop identifies all of the proteins in the dna sequence and prints them out (no offset)
            codon = dna[i:i+3] #split dna into groups of 3
            amino_acid = codon_table[codon]#holds amino acids that correspond to each codon
            proteins.append(amino_acid)#add the amino acid sequence to the protein list
            
    elif int(len(dna) % 3) != 0:#if not divisible by three
        new_dna = dna[:-1]#remove the last element in the string
        
        if int(len(new_dna)%3) == 0: #check to see if divisible by three again
            
            for i in range(0, len(new_dna), 3):#if divisible, make the list of protiens
                
                codon = new_dna[i:i+3]
                amino_acid = codon_table[codon]

                proteins.append(amino_acid)
                
        elif int(len(new_dna)%3) != 0: #checkes to see if divisible by three for a final time
            newer_dna = new_dna[:-1]#takes off last term if not divisible (this should make it fully devisible by three now)
            
            if int(len(newer_dna)%3) == 0: #since it is now divisible by three, the for loop creates a list of proteins (as was done above)
                for i in range(0, len(newer_dna), 3):
                    codon = newer_dna[i:i+3]
                    amino_acid = codon_table[codon]

                    proteins.append(amino_acid)

    return ''.join(proteins)#convert proteins to one string 

if translate(dna) == '':#checks for if the function translate ends up with no protein combos at all 
    print("NO PROTEINS IN RNA") #output statement

else:#prints output to user if there is protein combos
    print("Your RNA with no offset as protiens are...", translate(dna))

def translate_dna_offset_of_1(dna):#define function translate_dna_offset_of_1 - this function does the same as the one above however it is printing to an offset of one
    
    codon_table = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
} #initalize table
    
    proteins = []
    
    dna = dna[1:]#set it to an offset of one by removing first string character
    
    if int(len(dna) % 3) == 0:#specified above - repeats the same as previous function (checks if divisible by three)
        
        for i in range(0, len(dna), 3): #initalize for loop to determine the proteins in the strands of dna 
            codon = dna[i:i+3]
            amino_acid = codon_table[codon]
            
            proteins.append(amino_acid)
            
    elif int(len(dna) % 3) != 0:
        new_dna = dna[:-1]
        
        if int(len(new_dna)%3) == 0:
            
            for i in range(0, len(new_dna), 3):
                
                codon = new_dna[i:i+3]
                amino_acid = codon_table[codon]
                
                proteins.append(amino_acid)
                
        elif int(len(new_dna)%3) != 0:
            newer_dna = new_dna[:-1]
            
            if int(len(newer_dna)%3) == 0:
                for i in range(0, len(newer_dna), 3):
                    codon = newer_dna[i:i+3]
                    amino_acid = codon_table[codon]
        
                    proteins.append(amino_acid) 

    return ''.join(proteins) #turns it into a string

if translate_dna_offset_of_1(dna) == '':#checks if there are no protein combos that can be made
    print("NO PROTEINS WHEN RNA IS OFFSET OF ONE")

else:
    print("Your RNA with offset of one as protiens...", translate_dna_offset_of_1(dna))#output statement

def translate_dna_offset_of_2(dna): #same function as the previous two, just translates dna with an offset of 2 instead of 1 or none
    
    codon_table = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
}
    
    proteins = []
    
    dna = dna[2:] #set dna to an offset of two
    
    if int(len(dna) % 3) == 0:
        
        for i in range(0, len(dna), 3):
            codon = dna[i:i+3]
            amino_acid = codon_table[codon]
            
            proteins.append(amino_acid)
            
    elif int(len(dna) % 3) != 0:
        new_dna = dna[:-1]
        
        if int(len(new_dna)%3) == 0:
            
            for i in range(0, len(new_dna), 3):
                
                codon = new_dna[i:i+3]
                amino_acid = codon_table[codon]
                
                proteins.append(amino_acid)
                
        elif int(len(new_dna)%3) != 0:
            newer_dna = new_dna[:-1]
            
            if int(len(newer_dna)%3) == 0:
                for i in range(0, len(newer_dna), 3):
                    codon = newer_dna[i:i+3]
                    amino_acid = codon_table[codon]

                    proteins.append(amino_acid) 

    return ''.join(proteins)

if translate_dna_offset_of_2(dna) == '':#checks if there is no protein combos that can be made
    print("NO PROTEINS WHEN RNA IS OFFSET OF TWO")

else: #if there are proteins
    print("Your RNA with offset of 2 as protiens...", translate_dna_offset_of_2(dna))#output statement

print(" ")

print("Thats all folks! Goodbye! Thanks for using my code!")#goodbye statement
