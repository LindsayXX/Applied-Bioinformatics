from Bio import SearchIO
import re
import sys

file = open(sys.argv[2])
blast_results = SearchIO.read(file,"blast-xml")

for record in blast_results:
    min_exp = min(record.hsps.expect)
    min_exp_hsp = record.hsps[record.hsps.expect.index(min_exp)]
    if min_exp_hsp < 1e-20:
        if re.search(sys.argv[1],record.,re.IGNORECASE)
