import argparse
import re

def find_longest_repeating_subsequence(sequence):
    longest_subsequence = ""
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            substring = sequence[i:j]
            if sequence.count(substring) >= 2 and len(substring) > len(longest_subsequence):
                longest_subsequence = substring
    return longest_subsequence

def count_orfs(sequence):
    orf_pattern = re.compile(r'ATG(?:\w{3})*?(?:TAA|TAG|TGA)')
    orfs = orf_pattern.findall(sequence)
    return len(orfs)

def read_sequence_from_file(file_path):
    sequence = ""
    with open(file_path, "r") as file:
        for line in file:
            if not line.startswith(">") and not line.startswith("LOCUS") and not line.startswith("DEFINITION"):
                sequence += line.strip()
    return sequence

def main():
    parser = argparse.ArgumentParser(description="Find the longest repeating sub-sequence and count Open Reading Frames (ORFs) in a sequence.")
    parser.add_argument("file", type=str, help="Path to the input file in Fasta or GeneBank format")
    parser.add_argument("--duplicate", action="store_true", help="Find the longest repeating sub-sequence")
    parser.add_argument("--cORFs", action="store_true", help="Count Open Reading Frames (ORFs)")
    args = parser.parse_args()

    # Read the sequence from the input file
    sequence = read_sequence_from_file(args.file)

    # Perform the requested analysis
    if args.duplicate:
        longest_subsequence = find_longest_repeating_subsequence(sequence)
        if longest_subsequence:
            print(f"The longest repeating sub-sequence is: {longest_subsequence}")
        else:
            print("No repeating sub-sequence found in input")

    if args.cORFs:
        orf_count = count_orfs(sequence)
        print(f"Number of Open Reading Frames (ORFs): {orf_count}")

if __name__ == "__main__":
    main()
