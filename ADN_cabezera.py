from Bio.SeqIO import parse 
from Bio.SeqRecord import SeqRecord 
from Bio.Seq import Seq 

#file = open('NC_045512.fasta') 
file = open('NC_CP000138_converted.fasta')

records = parse(file, "fasta") 

for record in records:    
   print("Id: %s" % record.id) 
   print("Name: %s" % record.name) 
   print("Description: %s" % record.description) 
   print("Annotations: %s" % record.annotations) 
   #print("Sequence Data: %s" % record.seq) 
   #print("Sequence Alphabet: %s" % record.seq.single_letter_alphabet)
