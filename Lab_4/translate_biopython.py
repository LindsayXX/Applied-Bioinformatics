import os
from Bio import SeqIO
from Bio.Seq import Seq, translate
import sys

handle = open(sys.argv[1])
if os.stat(sys.argv[1]).st_size ==0:
	sys.exit('No sequences in the file!')

for seq_record in SeqIO.parse(handle, "fasta"):
	#if len(seq_record)==0:
	#	sys.exit('No sequences in the file!')
	print seq_record.id
	result = translate(seq_record)
	print result+'\n'
handle.close()
