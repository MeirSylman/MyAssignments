# Sequence Analysis Tool

This tool allows you to analyze DNA sequences to find the longest sub-sequence that apears twice, and count the number of Open Reading Frames (ORFs). The script can process input files in Fasta or GeneBank format.

## Features

- **Find Longest Repeating Sub-sequence**: Identifies the longest sub-sequence that appears at least twice in the given sequence.
- **Count Open Reading Frames (ORFs)**: Counts the number of ORFs in the sequence. ORFs are sequences that start with "ATG" and end with either "TAA", "TAG", or "TGA".

## Usage

To run the script, use the following command format in your terminal or command prompt:

```bash
python analyze.py FILE [--duplicate] [--cORFs]
```bash

### Arguments
FILE: Path to the input file in Fasta or GeneBank format.
--duplicate: Option to find the longest repeating sub-sequence in the sequence.
--cORFs: Option to count Open Reading Frames (ORFs) in the sequence.


What are Open Reading Frames (ORFs)?
Open Reading Frames (ORFs) are continuous stretches of codons that begin with a start codon (usually "ATG") and end with a stop codon (either "TAA", "TAG", or "TGA"). These sequences are important in the study of genes and protein synthesis because they potentially encode proteins.
