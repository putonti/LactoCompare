# Project LactoCompare
This repo includes scripts associated with the analysis of paired *Lactobacillus* samples from the female urogenital tract conducted in the work of Atkins *et al*. (under review).

## Abstract
**Evidence of *Lactobacillus* strains shared between the female urinary and vaginal microbiota**<br />
Haley Atkins, Baani Sabharwal, Leah Boger, Natalie Stegman, Alexander Kula, Alan J. Wolfe, Swarnali Banerjee, Catherine Putonti<br />

*Lactobacillus* species are common inhabitants of the “healthy” female urinary and vaginal communities, often associated with a lack of symptoms in both anatomical sites. Given identification by prior studies of similar bacterial species in both communities, it has been hypothesized that the two microbiotas are in fact connected. Here, we carried out whole genome sequencing of 49 *Lactobacillus* strains, which include 16 paired urogenital samples from the same participant. These strains represent five different *Lactobacillus* species: *L. crispatus*, *L. gasseri*, *L. iners*, *L. jensenii*, and *L. paragasseri*. Average nucleotide identity (ANI), alignment, single nucleotide polymorphism (SNP), and CRISPR comparisons between strains from the same participant were performed. We conducted simulations of genome assemblies and ANI comparisons and present a statistical method to distinguish between unrelated, related, and identical strains. We found that 50% of the paired samples have identical strains, evidence that the urinary and vaginal communities are connected. Additionally, we found evidence of strains sharing a common ancestor. These results establish that microbial sharing between the urinary tract and vagina is not limited to uropathogens. Knowledge that these two anatomical sites can share lactobacilli in females can inform future clinical approaches.


# Code Details

## resolve_crisprs.py
Code used to parse a file of CRISPR spacer sequences. The file was formatted as follows:
* Header: strain + "|" + Participant_ID + Time_of_Collection + Sample_Site
* Each spacer sequence listed on a new line following the header

## calculate_SNP.py
Code used to parse fasta-format alignment file to compute SNP%. Assumes pair-wise alignment file.

## subsampling.py
Code used to subsample reads and generate readsets for trimming (BBDuk) and assembly. Tools used by this script include:
* Seqtk : https://github.com/lh3/seqtk
* BBDuk (part of BBMap) : https://jgi.doe.gov/data-and-tools/software-tools/bbtools/bb-tools-user-guide/bbmap-guide/
* SPAdes : https://github.com/ablab/spades

## summary_file.rmd
R code used to generate distributions and conduct statistical tests for all *Lactobacillus* genomes evaluated.

