from Bio import SeqIO, AlignIO
import tempfile, subprocess
import sys

alignment= AlignIO.read(open(sys.argv[1]),"fasta")
num_bootstraps = sys.argv[2]
names = []

for j,seq_record in enumerate(alignment):
	names.append(seq_record.id)
	seq_record.id = 'seq%i' %j
	

#temp1=open("out.phy","w")
temp1 = tempfile.NamedTemporaryFile()
AlignIO.write(alignment,temp1,"phylip")
p=subprocess.Popen("phylip seqboot", stdin = open(sys.argv[1]),stdout = temp1)
m=p.communicate(stdin=sys.argv[1])#+'\nR'+str(num_bootstraps)+'Y\n')
