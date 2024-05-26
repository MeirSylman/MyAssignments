import pytest
from manipulating_csv.py import compute_stat


def test_compute(result_variance, result_mean):
    expected_variance = 3.5688415084138224e-06
    expected_mean = 0.01

    observd_variance = result_variance
    observd_mean = result_mean

    assert observd_variance == expected_variance
    assert observd_mean == expected_mean

