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


def test_compute(result_variance,result_mean):
    
    expected_variance = 3.5688415084138224e-06
    expected_mean = 0.01

    observd_variance = result_variance
    observd_mean = result_mean
    
    assert observd_variance == expected_variance
    assert observd_mean ==expected_mean

test_compute(process[0],process[1])
