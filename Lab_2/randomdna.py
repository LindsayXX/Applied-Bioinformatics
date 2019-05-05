import random

length=input('Length: ')
sequence=''
for i in range(0,length):
    sequence += random.choice('ATCG')
print('>randomsequence\n' + sequence)
