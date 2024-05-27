Folder content:

1. **expression_data.csv** - A file that holds an array of scRNA-seq output format, representing the different levels of expression for each of the investigated genes in the different cell types.

2. **manipulating_csv.py** - A Python script for analysis. The code normalizes the data and finds two main descriptive statistics of the values' distribution: the variance and the mean of the gene expression levels.

3. **test_expression_statistics.py** - A Python script for testing with the pytest package, validating that the analysis is performed correctly.
