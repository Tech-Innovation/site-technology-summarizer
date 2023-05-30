# Site Technology Summarizer

This script summarizes technologies related to a site based on an input Excel file. It performs certain operations on the data and generates an output Excel file with the summarized results.

## Prerequisites

Python 3.x
pandas library

## Usage

1. Ensure that you have Python 3.x installed on your system.
2. Install the required dependencies by running the following command:

    ``` bash
    pip install pandas
    ```

3. Prepare your input Excel file with the following considerations:
   * The input file must be in the .xlsx format.
   * If the file has a header, it should be present in the first row.
4. Execute the script using the command:

    ``` bash
    python summarize_technologies.py -i input_file.xlsx -o output_file.xlsx
    ```

    Replace input_file.xlsx with the path to your input file and output_file.xlsx with the desired name for the output file. The -o (or --output) argument is optional, and if not provided, the output file will be named "output.xlsx" by default.

5. The script will process the input file and generate the summarized output.
6. The resulting output file will be saved in the same directory as the input file, with the provided name or a modified name if necessary.

## Test Usage

In the work folder you will find a test_data.xlsx file that you can use to test the script. The file contains a header row and some sample data. You can run the script on this file using the following command:

``` bash
python summarize_technologies.py -i work/test_data.xlsx -o test_output.xlsx -h
```

The use of the work folder is optional. You can process any file from any location on your system.

## Command-line Arguments

The script accepts the following command-line arguments:

* -i or --input: (required) Path to the input Excel file.
* -o or --output: Path and name of the output Excel file. If not provided, the default name "output.xlsx" will be used.
* -h or --header: Indicates whether the input file has a header. Include this flag if the file contains a header row.

## Output

The script performs the following operations on the input data:

1. Selects the first two columns from the input data.
2. Removes rows with empty values in the second column (h2).
3. Converts values in the first column (h1) to uppercase.
4. Groups the values in the second column (h2) by the unique values in the first column (h1) and sorts them in a specific order.
5. Removes duplicate rows from the resulting data.
6. Prints the first five rows of the resulting data to the console.
7. Saves the resulting data as an Excel file with the specified name or the default name "output.xlsx".

The generated output Excel file will contain the summarized data based on the performed operations.

Note: The script assumes that the pandas library is installed and accessible in the Python environment.