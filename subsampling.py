path_in='/scratch/data/' # note change this to your directory of fastq data
path_out='/home/cputonti/subsamples/' # note change this to the directory where you want to write results
path_software='/home/cputonti/Software/' # note change this to the directory where software executables/scripts are located

import glob
import random
import gzip
import os
from subprocess import check_output

files=glob.glob(path_in+'*')
a=[i for i in files if '.fastq' in i]

def wc(filename):
    return int(check_output(["wc", "-l", filename]).split()[0])
 
fi=0
while fi<len(a):
    file1=a[fi]
    file2=a[fi+1]

    x=wc(file1)
    number_reads=int(x/4)
    random.seed(1)
    randomList=random.sample(range(0,number_reads),50)
    counter=1
    lpath=len(path_in)
    if path_in2 in file1 or path_in3 in file2:
        lpath+=1
    
    for i in randomList:
        # note, 150000 was chosen for 20x coverage based upon knowledge of sequencing depth and genome size.
        command = path_software+'seqtk/seqtk sample -s'+str(i)+' '+file1+' 150000 > '+path_out+str(counter)+'_'+file1[lpath:]
        os.system(command)

        command = path_software+'seqtk/seqtk sample -s'+str(i)+' '+file2+' 150000 > '+path_out+str(counter)+'_'+file2[lpath:]
        os.system(command)

        command = path_software+"bbmap/bbduk.sh -Xmx1G overwrite=t in1="+path_out+str(counter)+'_'+file1[lpath:]+" in2="+path_out+str(counter)+'_'+file2[lpath:]+" out1="+path_out+str(counter)+'_trimmed_'+file1[lpath:]+" out2="+path_out+str(counter)+'_trimmed_'+file2[lpath:]+" qtrim=rl ftl=15 ftr=135 maq=20 maxns=0 stats="+path_out+str(counter)+'_trimmed_'+file2[lpath:]+".stats statscolumns=5 trimq=20"
        os.system(command)
        #outfile.write(command+'\n')

        command = "python "+path_software+"SPAdes-3.15.4-Linux/bin/spades.py --only-assembler -t 10 -1 "+path_out+str(counter)+'_'+file1[lpath:]+" -2 "+path_out+str(counter)+'_'+file2[lpath:]+" -o "+path_out+str(counter)+'_'+file1[lpath:file1.find("_R1")]+"_assembly"
        os.system(command)

        #renaming and moving the spades output before I blow away the spades stuff that isn't needed
        command = "cp "+path_out+str(counter)+'_'+file1[lpath:file1.find("_R1")]+"_assembly/contigs.fasta "+path_out+str(counter)+'_'+file1[lpath:file1.find("_R1")]+"_contigs.fasta"
        os.system(command)

        #cleaning up the folder that isn't needed
        command = "rm -r "+path_out+str(counter)+'_'+file1[lpath:file1.find("_R1")]+"_assembly"
        os.system(command)
        
        #cleaning up the files that aren't needed
        command = "rm "+path_out+str(counter)+'_'+file1[lpath:]
        os.system(command)

        #cleaning up the files that aren't needed
        command = "rm "+path_out+str(counter)+'_'+file2[lpath:]
        os.system(command)

        counter+=1
    fi+=2

        
