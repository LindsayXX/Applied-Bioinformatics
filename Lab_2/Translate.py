import sys

def reading(file):
    accessions = []
    sequences = []
    new_sequence=0
    for line in file.split('\n'):
        if line != '' and line[0] == '>':
            accessions.append(line.split(' ')[0][1:len(line)])
            new_sequence=1
        elif line!='' and new_sequence == 1:
            sequences.append(line.upper())
            new_sequence=0
        elif (line != ''):
            sequences[len(sequences)-1] += line.upper()
    return accessions, sequences


def fastaprint(name, seq):
    print('>' + name)
    print(linesplit(seq))


def linesplit(sequence):
    split_seq = ''
    length = len(sequence)
    if (length > 60):
        for i in range(length // 60 + 1):
            split_seq += (sequence[0 + i * 60:min(length, (i + 1) * 60)] + '\n')
    else:
        split_seq = (sequence + '\n')
    return split_seq

def find_orf(sequence):
    if len(sequence)<3:
        start_indices=[0]
    else:
        stop_codon_indices=[-3,-2,-1]
        for j in range(len(sequence)-2):
            if sequence[j:j + 3] == 'TAA' or sequence[j:j + 3] == 'TAG' or sequence[j:j + 3] == 'TGA':
                stop_codon_indices.append(j)
        stop_codon_indices.extend((len(sequence)-2, len(sequence)-1, len(sequence)))
        max_length = -1
        start_indices=[]
        for l in range(len(stop_codon_indices)-3):
            for n in range(l+1,len(stop_codon_indices)):
                if (stop_codon_indices[n]-stop_codon_indices[l])%3==0 and stop_codon_indices[l]+6 <= len(sequence):
                    if (stop_codon_indices[n]-stop_codon_indices[l])>max_length :
                        max_length=(stop_codon_indices[n]-stop_codon_indices[l])
                        start_indices=[stop_codon_indices[l]+3]
                    elif (stop_codon_indices[n]-stop_codon_indices[l])==max_length:
                        start_indices.append(stop_codon_indices[l]+3)
                    break

    return start_indices

def translate(sequence):
    table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TGC': 'C', 'TGT': 'C',
        'TGG': 'W',
    }
    protein = ""
    for i in range(0, len(sequence)-2, 3):
        codon = str(sequence[i:i + 3])
        if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
            break
        elif codon in table:
            protein += table[codon]
        else:
            protein += 'X'
    return protein


with open(sys.argv[1], 'r') as f:
    content = f.read()
acc, seq = reading(content)
prot_seq=[]
counter=0
for seq_nr in range(len(seq)):
    starts = find_orf(seq[seq_nr])
    for t, start in enumerate(starts):
        prot_seq.append(translate(seq[seq_nr][start:]))
        if t > 0:
            acc.insert(seq_nr+counter+1, acc[seq_nr+(counter-t+1)]+'_version_'+str(t))
            counter += 1
for i in range(len(acc)):
    fastaprint(acc[i], prot_seq[i])
