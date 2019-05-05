import matplotlib.pyplot as plt
import argparse as ap
import sys
from Bio.Blast import NCBIXML

parser = ap.ArgumentParser()
parser.add_argument("input_file",  nargs='?', help = "Blast results in XML format", type=ap.FileType('r'), default=sys.stdin)
parser.add_argument("output_name", help = "name for the file that will contain the histogram" ,type=str)
args = parser.parse_args()


def getscores(blast_records):
	scores = []
	evalue = []
	for blast_record in blast_records:
		for alignment in blast_record.alignments:
				for hsp in alignment.hsps:
					evalue.append(hsp.expect)
					scores.append(hsp.bits)
	return scores

def visualize(scores):
	plt.figure()
	plt.hist(scores,bins=20)
	plt.xlabel('Score')
	plt.ylabel('Number of sequences')
	#plt.show()


def outputfile(outfile):
	plt.savefig(outfile,format='pdf')
	

# main
blast_records = NCBIXML.parse(args.input_file)
scores = getscores(blast_records)
#print(scores)
visualize(scores)
outfile = args.output_name
#outfile = 0
outputfile(outfile)
