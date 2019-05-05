from Bio.Blast import NCBIWWW
from Bio import SeqIO
import sys

sequence = SeqIO.read(open(sys.argv[1]), format="fasta")
result = NCBIWWW.qblast("blastp","nr",sequence.seq,format_type="XML")
print(result.read())