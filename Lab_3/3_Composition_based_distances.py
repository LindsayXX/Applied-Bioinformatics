import sys
import math as m
from collections import OrderedDict

def reading(in_file,filename):
	sequence = ''
	name = ''
	flag = 0
	for line in in_file.split('\n'):
		if (line.startswith('>')):
			flag += 1
			if flag>1 :
				#print('More than one sequence in '+filename+'!', file=sys.stderr)
				#sys.stderr.write('More than one sequence in '+filename+'!\n')
				sys.exit('More than one sequence in '+filename+'!')
			word = line.split(' ')
			name = word[0][1:11]
		else:
			sequence+=line
	return sequence, name

def counting(sequence):
	num = [0,0,0,0]
	fre = [0,0,0,0]
	nuc = ['A','T','C','G']
	j = 0
	for i in nuc:
		num[j] = sequence.count(i)
		j += 1
	for k in range(4):
		fre[k] = num[k]/(sum(num)*1.0)
		
	return fre

def dist(pix,piy):
	diff = 0
	for i in range(4):
		diff += (pix[i]-piy[i])**2
	diff = m.sqrt(0.25 * diff)
	return diff

def matrix(fre,name):
	matrix = OrderedDict()
	for i in range(len(fre)):
		res = []
		for j in range(len(fre)):
			res.append(dist(fre[i],fre[j]))
		matrix[name[i]] = res
		#print(' '.join(res))
	print(len(fre))
	for k in matrix.keys():
		print k.ljust(10)+' '.join([str('%.3f' %x)for x in matrix[k]])

fre = []
name_list = []
if len(sys.argv)==1:
	sys.exit('No sequences to compare!')
if len(sys.argv)==2:
	sys.exit('Only one file given!')
else:
	for i in range(1,len(sys.argv)):
		with open(sys.argv[i],'r') as f:
			content=f.read()
		sequence, name =reading(content,sys.argv[i])
		name_list.append(name)
		fre.append(counting(sequence))
		#print(counting(sequence))
	matrix(fre,name_list)
	
	

