import sys


def reading(file):
	sequence = ''
	for line in file.split('\n'):
		if (line.startswith('>')):
			continue
		else:
			sequence+=line
	return sequence

def counting(sequence):
	number=sequence.count('G')+sequence.count('C')
	content = number/(len(sequence)*1.0)
	return content
	
for i in range(len(sys.argv)):
	with open(sys.argv[i],'r') as f:
		content=f.read()
	sequence=reading(content)
	gc_content=counting(sequence)
	print('%.3f' % gc_content)


