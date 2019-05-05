import sys
import re
from Bio import SeqIO
from Bio import motifs

def motif(record):
	seq = str(record)
	return re.search(r'KL[EI]{2,}K',seq)

#	if (seq.find("KL")>-1):
#		ind = seq.index("KL")
#		if(seq[ind+2] == "E" or seq[ind+2] =="I"):
#			if(seq[ind+3] == "E" or seq[ind+3] =="I"):
#				for e_i_index in range(len(seq)-ind-3):
#							if(seq[ind+4+e_i_index] == "K"):
#								return True
#							elif(seq[ind+4+e_i_index] != "E" and seq[ind+4+e_i_index] !="I"):
#								return False
#			else:
#				return False
#		else:
#			return False
#	else:
#		return False
				

handle = open(sys.argv[1])
alignment = SeqIO.parse(handle,"fasta")
num = 0
for record in SeqIO.parse(handle, "fasta"):
	if(motif(record.seq)):
		num += 1
		print('>' + record.id + " This sequence contains KLEEK")
		print(record.seq)
	#else:
		#print(record.id + "There is no KLEEK-like motif in this sequence")


#motifs.create("KLEEK",alphabet= None)
#print(motifs)

handle.close()
