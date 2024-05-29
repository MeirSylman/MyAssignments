import pandas as pd
import pytest

def compute_stat(path):
    df = pd.read_csv(path)
    df.set_index('Unnamed: 0', inplace=True)
    # normalization:
    for column in df.columns:
        if type(df[column]) != str:
            sum_column = df[column].sum()
            df[column] = df[column] / sum_column

    print('Data normalized.\n Calculating genes means statistics.')

    gene_means = df.mean(axis=1)
    variance = gene_means.var()
    mean = gene_means.mean()

    print(f"\nVariance of the gene means: {variance}")
    print(f"\nMean of the gene means: {mean}")
    return variance, mean

path = "expression_data.csv"
process= compute_stat(path)
