from manipulating_csv import compute_stat


def test_compute_stat():
    path = "expression_data.csv"
    expected_variance = 3.5688415084138224e-06
    expected_mean = 0.01

    variance, mean = compute_stat(path)

    assert variance == expected_variance, f"Expected variance: {expected_variance}, but got: {variance}"
    assert mean == expected_mean, f"Expected mean: {expected_mean}, but got: {mean}"
