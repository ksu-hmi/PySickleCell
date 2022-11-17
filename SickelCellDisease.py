
def translate(seq, dict): #translate takes the sequence of codon's as argument and the dictionary from which the amino acids will be fetched
    start = 0 #starting point of the word selection
    end = 3 #Ending point of the word selection, as codon's are represented by three characters
    print("--------------------------------------------------------")
    print("Your Amino Acid Sequence is as follows: ")
    print("--------------------------------------------------------")
    for char in seq: #Looks at the sequence char for char
        word = seq[start:end] #Creates a word of three letters 
       # print()
        #print("Your word is: ", word)
        if end >= len(seq) + 1: 
            break
        
        if word not in dict.keys(): #If the word does not exist in the library changes the word / key to X 
            word = "X"
        
        for key in dict.keys(): #Whatever the word is at time of the loop, will go through the dictionary and print out the value of the key
            
            if word == key: 
                print(dict[key], end = "")
        #print("word", word)
        start += 3 #Increment both the start and the end to move up in the string
        end += 3
        
    print()
                   
def mutate(filepath): #function takes a filepath name as an argument
    print("--------------------------------------------------------")
    print("NormalDNA printout:")
    print("--------------------------------------------------------")
    with open (filepath, "r+") as f, open (normalDNA, "a+") as nf1: #Opens up the text file and creates a new file normalDNA.txt
        file1Data = f.read().replace('\n', '') #replaces the newline spacing with nothing to make it into one string
        newFile1Data = file1Data.replace("a", "A") #replaces small letter a with a upper case A
        
        print(newFile1Data)
        nf1.write(newFile1Data) #Prints the new codon's with the replaced letter to a text file called normalDNA.txt
        
        print("--------------------------------------------------------")
        print("MutatedDNA printout:")
        print("--------------------------------------------------------")
        with open (filepath, "r+") as f, open (mutatedDNA, "a+") as nf2: #Same principle as the previous opening of file
            file2Data = f.read().replace('\n', '') #removes the new line spacing
            newFile2Data = file2Data.replace("a", "T" ) #replaces small letter a with the capital letter T
                
            print(newFile2Data)   
            nf2.write(newFile2Data) #Writes out the new codon onto a text file called mutatedDNA.txt
            
def txtTranslate():
    with open  (normalDNA, "r+") as f, open(mutatedDNA, "r+") as f1: #opens up the two new text files that was created by the mutate function and calls the translate function
      normalDNAData = f.read()
      translate(normalDNAData, my_dict) #normalDNA text file translation
    
      mutatedDNAData = f1.read()
      translate(mutatedDNAData, my_dict) #Mututated text file translation

if __name__ == "__main__": 
    
    #Creation of variables to make the text documents easier to use in the functions
    filepath = "DNA.txt"
    normalDNA = "normalDNA.txt"
    mutatedDNA = "mutatedDNA.txt"
    my_dict = { #Creation of the dictionary from which the codon's will be read and then printing out the value of the key
            
        "ATT" : "Isoleucine",
        "ATC" : "Isoleucine",
        "ATA" : "Isoleucine",
        "CTT" : "Leucine",
        "CTC" : "Leucine",
        "CTA" : "Leucine",
        "CTG" : "Leucine",
        "TTA" : "Leucine",
        "TTG" : "Leucine",
        "GTT" : "Valine",
        "GTC" : "Valine",
        "GTA" : "Valine",
        "GTG" : "Valine",
        "TTT" : "Phenylalanine",
        "TTC" : "Phenylalanine",
        "ATG" : "Methionine",
        "X"   : "X"
        
        }
    
   
    #seq = "ATTATTATTYUIIUYIYUIATTIUYATTIUYUYATTTTATATTTATAATTTTATATTTATAT"
    #translate(seq, my_dict)
    
    mutate(filepath) #Calls the mutate function to start the replacement of the letters
    txtTranslate() #Calls the translate function with the two new text files to start the amino acid translation
inputfile ="DNA_sequence_.txt"
f = open(inputfile, "r")
seq = f.read()
  
seq = seq.replace("\n", "")
seq = seq.replace("\r", "")
# import random library
import random

# function to generate dna strands
def generateDNASequence():
	
	# list of available DNA bases
	l = ['C', 'A', 'G', 'T']
	res = ""
	for i in range(0, 40):
		# creating the DNA strand by appending
		# random characters from the list
		res = res + random.choice(l)
	return res

# function to alter dna strands
def applyGammaRadiation(dna):
	
	# possibility of mutation is generated randomly
	pos = random.randint(1, 100)
	cdna = ''
	
	# list of available DNA bases
	l = ['C', 'A', 'G', 'T']
	
	# if the possibility of mutation generated randomly
	# is >100 then mutation happens
	if (pos > 100):
		
		# the position where mutation will take place
		# is chosen randomly
		changepos = random.randint(0, 39)
		dl = []
		
		# the characters in DNA strand is converted to list
		dl[:0] = dna
		
		# the character at the determined mutation position
		# is fetched.
		ch = "" + dl[changepos]
		
		# since the fetched character should be different from
		# the one replacing it we remove the fetched character
		# from the list of available choices for choosing another
		# character in its place
		l.remove(ch)
		
		# the new character or DNA base is chosen from the list
		ms = random.choice(l)
		cl = []
		
		# DNA strand characters are again appended to a new list
		cl[:0] = dna
		
		# the new base in the mutated position is set
		cl[changepos] = ms
		
		# the characters in the cl list is converted to string again
		# this is the new mutated DNA string
		cdna = ''.join([str(e) for e in cl])
	

# function to detect mutation
def detectMutation(dna, cdna):
	count = 0
	
	# x and y take each character in dna and cdna
	# for character by character comparison
	for x, y in zip(dna, cdna):
		
		# if the character at the same index match
		# then the count is increased
		if x == y:
			count = count + 1
		
		# incase of mismatch the loop is broken
		else:
			break

	# the count value points to the index before the
	# position of mutation
	return count


dna = generateDNASequence()
print(dna+" (Original DNA)")
cdna = applyGammaRadiation(dna)
print(cdna+" (DNA after radiation)")
count = detectMutation(dna, cdna)

# if count=40 it means all the characters of the 2 strands match
# hence no mutation
if count == 40:
	print("No Mutation detected")

# if count is less than 50
# it means mutation has occurred
else:
	
	# ^ denotes the position of mutation
	pos = "^"
	print(pos.rjust(count+1))
	print("Mutation detected at pos = ", (count+1))
