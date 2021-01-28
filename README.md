# ud-bioinformatics-research-SARS-CoV-2
Computational biology research of SARS-CoV-2 phylogenetics.

University of Dallas, Irving, TX
Spring 2021
This repository contains code and other related materials.
A summary of the code is, primarily, a SARS-CoV-2 Phylogenetic Classification Model for Computational Biology Research.
Other programs do other functions, such as select random subset of NCBI data sets.

Advisors: Dr. Robert Hochberg and Dr. Inimary Toby

Description: Build a computational model to classify viral strains of SARS-CoV-2. Implement phylogenetic pattern recognition to map sequence data types to biological systems. Co-design solutions and diagnostics for research in biomarkers. Collaborate and participate in research with a community of machine learning engineers and other researchers. Assist the research community to publish, present, and distribute teachable resources based on the research.


The following text is copied from the UD Bioinformatics Club Repository README, for historical reasons:

# ud-bioinformatics-club
University of Dallas Bio Informatics Club

## Friday, March 27th 2020:

Group 1 (Michael and Kaitlyn). Obtain all SARS Coronavirus 2 sequences in GenBank as a DNA FASTA File and as a Protein FASTA file

Group 2 (Joseph and Gretta). Decide what software will be used to analyze protein coding sequences (CD-HIT) or functional characteristics of protein FASTA file

## Friday, April 3rd 2020:

*Gameplan*
1. Make phylogenetic tree of all COVID-19 sequences and BLAST (non-COVID-19) sequences (Kaitlyn)
2. Perform CD-HIT analysis on protein coding (or non-coding) sequences (Christian)
3. Find motif differences between clusters (Joseph)

## Friday, April 10, 2020:
1) Kaitlyn - filter for final strains to be used in analysis (strains will be filtered based on geographical location information) and add extra strains from Dr. Toby's initial tree + Alphacoronavirus, murine, pigeon, mouse, bat from "Coronavirus" search in Genbank
2) Kaitlyn - mass phylogenetic assessment
3) Everyone - take a look at clades and look for interesting patterns
4) Joseph/Christian - Use accession # from Kaitlyn's tree strains, download protein FASTAs for each accession #, and merge all files into 1.
5) Christian - Perform CD-HIT on mother-of-all FASTA and change cutoff to see how # of clusters changes.

## Friday, April 17, 2020:
Redo analyses for April 10th with corrected protocols.

## Friday, April 24, 2020:
1) Add your individual methods/figures to Google Doc
2) Kaitlyn - Add 2 extra MERS and 2 extra SARS (HUMAN INFECTIONS) to pool
3) Christian - Add Kaitlyn's new accessions to MOAs and parse using Jupyter
