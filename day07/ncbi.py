from Bio import Entrez
import sys
import os
import csv
from datetime import datetime


Entrez.email = "msylman@gmail.com"

def search_ncbi_database(term, max_results, db="nucleotide"):
    handle = Entrez.esearch(db=db, term=term, retmax=max_results)
    record = Entrez.read(handle)
    handle.close()
    return record['IdList'], record['Count']


def import_data(id_list, db="nucleotide"):
    ids = ",".join(id_list)
    handle = Entrez.efetch(db=db, id=ids, rettype="gb", retmode="text")
    records = handle.read()
    handle.close()
    return records.split("\n\n")


def save_records_to_files(records, term, requested_number, total_found):
    os.makedirs('downloads', exist_ok=True)
    file_names = []

    for i, record in enumerate(records):
        file_name = f"downloads/{term}_{i + 1}.txt"
        with open(file_name, 'w') as file:
            file.write(record)
        file_names.append(file_name)

    metadata_file = "downloads/metadata.csv"
    with open(metadata_file, 'a', newline='') as csvfile:
        fieldnames = ['Date', 'Search Term', 'Max Number Requested', 'Total Found']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if csvfile.tell() == 0:
            writer.writeheader()
        writer.writerow({'Date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                         'Search Term': term,
                         'Max Number Requested': requested_number,
                         'Total Found': total_found})

    return file_names


def main():
    if len(sys.argv) != 3:
        print("Usage: python ncbi.py TERM NUMBER")
        sys.exit(1)

    term = sys.argv[1]
    number = int(sys.argv[2])

    id_list, total_found = search_ncbi_database(term, number)
    records = import_data(id_list)
    file_names = save_records_to_files(records, term, number, total_found)

    for file_name in file_names:
        print(file_name)


if __name__ == "__main__":
    main()
