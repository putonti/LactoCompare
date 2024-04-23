file='crispr_spacer_file.txt' # note change this to your file

with open(file,'r') as f:
    lines=f.readlines()
lines=[i.strip() for i in lines]

spacers=dict() #dictionary of spacers by sample (participant, collection time, genome)
samples=set() # samples (participant and collection time)

# reverse complement of spacer. Need to consider rc because genomes are contigs. Don't
# know what strand is represented in the contig
def rc(x):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverse_complement = "".join(complement.get(base, base) for base in reversed(x))
    return reverse_complement

# parse crispr spacer file
index=0
while index<len(lines):
    if len(lines[index])>1:
        if lines[index][0]=='>':
            x=lines[index].split(' ')
            genome=(x[4],x[5],x[6])
            spacers[genome]=[]
            samples.add((x[4],x[5]))
            i=index+1
            while i<len(lines):
                spacers[genome].append(lines[i])
                spacers[genome].append(rc(lines[i]))
                i+=1
                if i<len(lines):   
                    if len(lines[i])>0:
                        if lines[i][0]=='@':
                            i=len(lines)
                    else:
                        i=len(lines)
    index+=1

for i in spacers:
    spacers[i].sort()

num_spacers_by_sample=dict()
spacers_by_sample=dict()
for i in samples:
    num_spacers_by_sample[i]=0
    spacers_by_sample[i]=set()

for i in spacers:
    x,y,z=i
    num_spacers_by_sample[(x,y)]+=1
    spacers_by_sample[(x,y)].add(tuple(spacers[i]))

for i in samples:
    print(i,num_spacers_by_sample[i],len(spacers_by_sample[i]))
