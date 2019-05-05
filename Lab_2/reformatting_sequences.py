import sys
import pdb

def reading(file):
	accessions = []
	sequences = []
	for line in file.split('\n'):
		if (line != '' and line[0] != '#' and line[0] != '/'):
			accessions.append(line.split()[0])
			if (len(line.split())<=1):
				sequences.append('')
			else:
				sequences.append(line.split()[1])
	return accessions, sequences

def fastaprint(name,seq):
	print('>'+name)
	print(linesplit(seq))

def linesplit(sequence):
	split_seq = ''
	length = len(sequence)
	if(length>60):
		for i in range(length/60 + 1):
			split_seq+=(sequence[0+i*60:min(length,(i+1)*60)]+'\n')
	else:
		split_seq = (sequence + '\n')
	return split_seq

with open(sys.argv[1],'r') as f:
	content=f.read()
accessions,sequences = reading(content)
for i in range(len(accessions)):
	fastaprint(accessions[i],sequences[i])
