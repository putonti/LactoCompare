from Bio import SeqIO

file='alignment.fasta' # note change this to your alignment file

records = list(SeqIO.parse(file, 'fasta'))

participant1 = str(records[0].seq)
participant2 = str(records[1].seq)

count_one_snp = 0
count_one_bases = 0

for i in range(0, len(participant1)):
    if participant1[i] != participant2[i] and (participant1[i] != 'N' and participant2 != 'N'):
        count_one_snp+=1

    if participant1[i] != 'N' and participant2[i] != 'N':
        count_one_bases+=1
snp_ratio = count_one_snp/count_one_bases
print('1 and 2: ' +str(count_one_snp)+'/'+str(count_one_bases)+' = '+str(snp_ratio))
