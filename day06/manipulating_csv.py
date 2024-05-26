import pandas as pd
import sys
import pytest

def compute_stat(path, filename='expression_data.csv'):
    file_path = f"{path}/{filename}"
    df = pd.read_csv(file_path)

    # normalization:
    for column in df.columns:
        sum_column = df[column].sum()
        df[column] = df[column] / sum_column

    print('Data normalized.\n Calculating genes means statistics.')

    gene_means = df.mean(axis=1)
    variance = gene_means.var()
    mean = gene_means.mean()

    print(f"\nVariance of the gene means: {variance}")
    print(f"\nMean of the gene means: {mean}")
    return variance, mean

path = sys.argv[1]
process= compute_stat(path)


