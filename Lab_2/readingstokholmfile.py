import sys
with open(sys.argv[1],'r') as f:
	content=f.read()
num = 0
accessions = ''
for line in content.split('\n'):
	if (line != '' and line[0] != '#' and line[0] != '/'):
		num += 1
		accessions += (line.split()[0] + '\n')
print(num)
print(accessions)



