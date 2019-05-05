import pexpect, tempfile
import sys, os
from Bio import Phylo, AlignIO

alignment= AlignIO.read(open(sys.argv[1]),"fasta")
num_bootstraps = sys.argv[2]
names = []
#path = "/home/k/l/klier/Documents/AppBio/dd2404_ab/Lab_3/Advanced_2"
path = "/home/l/i/lingxi/Applied_Bio/dd2404_ab/Lab_3/Advanced_2"

# Renaming sequences
for j,seq_record in enumerate(alignment):
	names.append(seq_record.id)
	seq_record.id = 'seq%i' %j

# seqboot
temp1 = tempfile.NamedTemporaryFile(delete=False, dir=path)
AlignIO.write(alignment,temp1,"phylip")
temp1.close()
os.rename(temp1.name,'infile') # temp1 is now called infile
temp2 = tempfile.NamedTemporaryFile(delete=False, dir=path)
os.rename(temp2.name,'outfile') # temp2 is now called outfile
p1 = pexpect.spawn("phylip seqboot")
p1.expect('Y to accept these or type the letter for one to change')
p1.sendline('R')
p1.expect('Number of replicates?')
p1.sendline(str(num_bootstraps))
p1.sendline('Y')
p1.sendline(str(37))
p1.expect('(please type R, A, F, or Q)')
p1.sendline('A')
p1.expect('Done')
p1.close()
temp2.close()

# protdist
temp3 = tempfile.NamedTemporaryFile(delete=False, dir=path)
os.unlink('infile') # temp1 deleted
os.rename('outfile','infile') # temp2 is now called infile
os.rename(temp3.name,'outfile') # temp3 is now called outfile
p2 = pexpect.spawn("phylip protdist")
p2.expect('(please type R, A, F, or Q)')
p2.sendline('A')
p2.expect_exact('Are these settings correct? (type Y or the letter for one to change)')
p2.sendline('M')
p2.expect_exact('Multiple data sets or multiple weights? (type D or W)')
p2.sendline('D')
p2.expect_exact('How many data sets?')
p2.sendline(str(num_bootstraps))
p2.expect_exact('Are these settings correct? (type Y or the letter for one to change)')
p2.sendline('Y')
p2.expect('Done')
p2.close()
temp3.close()

# neighbor
temp4 = tempfile.NamedTemporaryFile(delete=False, dir=path)
temp5 = tempfile.NamedTemporaryFile(delete=False, dir=path)
os.unlink('infile') # temp2 deleted
os.rename('outfile','infile') # temp3 is now called infile
os.rename(temp4.name,'outfile') # temp4 is now called outfile
os.rename(temp5.name,'outtree') # temp5 is now called outtree
p3 = pexpect.spawn("phylip neighbor")
p3.expect('(please type R, A, F, or Q)')
p3.sendline('A')
p3.expect('Y to accept these or type the letter for one to change')
p3.sendline('M')
p3.expect_exact('How many data sets?')
p3.sendline(str(num_bootstraps))
p3.sendline(str(37))
p3.expect('Y to accept these or type the letter for one to change')
p3.sendline('Y')
p3.expect('(please type R, A, F, or Q)')
p3.sendline('A')
p3.expect('Done')
p3.close()
temp4.close()
os.unlink('outfile') # temp4 deleted
temp5.close()

# consense
temp6 = tempfile.NamedTemporaryFile(delete=False, dir=path)
temp7 = tempfile.NamedTemporaryFile(delete=False, dir=path)
os.unlink('infile') # temp3 deleted
os.rename('outtree','intree') # temp5 is now called intree
os.rename(temp6.name,'outfile') # temp6 is now called outfile
os.rename(temp7.name,'outtree') # temp7 is now called outtree
p4 = pexpect.spawn("phylip consense")
p4.expect('(please type R, A, F, or Q)')
p4.sendline('A')
p4.expect_exact('Are these settings correct? (type Y or the letter for one to change)')
p4.sendline('Y')
p4.expect('(please type R, A, F, or Q)')
p4.sendline('A')
p4.expect('Done')
p4.close()
temp6.close()
temp7.close()

os.unlink('intree') # temp5 deleted
os.unlink('outfile') # temp6 deleted

# Renaming sequences in the tree
tree = Phylo.read('outtree','newick')
for element in tree.find_elements():
	if element.name != None:
		element.name = names[int(str(element.name)[3:])]
Phylo.write(tree,sys.stdout,'newick')

os.unlink('outtree') # temp7 deleted

