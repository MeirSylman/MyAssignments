# NCBI Data Downloader

## Usage

This tool allows you to search for a term in the NCBI nucleotide database and download a specified number of items. Each downloaded item is saved in its own file, and metadata about the search is recorded in a CSV file.

### How to Run the Script


**Run the script with the following command:**

    ```bash
    python ncbi.py "SEARCH_TERM" NUMBER
    ```

    - `SEARCH_TERM`: The term you want to search for in the NCBI database.
    - `NUMBER`: The maximum number of items you want to download.

### Example Usage

To search for "Escherichia" and download 5 items, use the following command:

```bash
python ncbi.py Escherichia 5
