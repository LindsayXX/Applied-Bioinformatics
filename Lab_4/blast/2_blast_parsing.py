import sys
import re
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.Blast import NCBIWWW
from math import e

from Bio.Blast import NCBIXML
blast_records = NCBIXML.parse(open(sys.argv[2]))
counter = 0

for blast_record in blast_records:
    for alignment in blast_record.alignments:
        if re.search(sys.argv[1],alignment.title,re.IGNORECASE):
            evalue = 1e-19
            score = 0
            for hsp in alignment.hsps:
                if(hsp.expect<evalue):
                    evalue = hsp.expect
                    score = hsp.bits
            if evalue <= 1e-20:
		counter += 1
                print("%7s  %20s  %3.1f  %2.1e " % (blast_record.query, alignment.hit_def[0:19],  score, evalue))
if counter == 0:
	sys.stderr.write("Warning: No hits\n")
