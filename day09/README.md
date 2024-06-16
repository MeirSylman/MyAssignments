# Sequence Analysis Tool

This tool allows you to analyze DNA sequences to find the longest repeating sub-sequence and count the number of Open Reading Frames (ORFs). The script can process input files in Fasta or GeneBank format.

## Features

- **Find Longest Repeating Sub-sequence**: Identifies the longest sub-sequence that appears at least twice in the given sequence.
- **Count Open Reading Frames (ORFs)**: Counts the number of ORFs in the sequence. ORFs are sequences that start with "ATG" and end with either "TAA", "TAG", or "TGA".

## Requirements

- Python 3.x
- argparse (standard library)
- re (standard library)

## Installation

Ensure you have Python 3.x installed on your system. If not, download and install it from [python.org](https://www.python.org/).

There are no external dependencies required for this script.

## Usage

Save the script to a file, for example, `analyze.py`.

To run the script, use the following command format in your terminal or command prompt:

```bash
python analyze.py FILE [--duplicate] [--cORFs]
