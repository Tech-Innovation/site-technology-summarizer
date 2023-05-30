import argparse
import pandas as pd
from pathlib import Path


def args_parser():
    parser = argparse.ArgumentParser(
        description="Summarize technologies related to a site", add_help=False
    )
    parser.add_argument("-i", "--input", help="Path to the excel file", required=True)
    parser.add_argument(
        "-o", "--output", help="Custom name for the output file", default="output.xlsx"
    )
    parser.add_argument(
        "-h",
        "--header",
        help="Whether the input file has a header",
        action="store_true",
    )
    args = parser.parse_args()

    return args


def io(input_file_path_str, output_file_name):
    input_file_path = Path(input_file_path_str)
    if not input_file_path.exists():
        raise FileNotFoundError("Input file does not exist")
    if input_file_path.suffix != ".xlsx":
        raise ValueError("Input file must be an .xlsx file")

    output_file_path = Path(output_file_name)
    if output_file_path.suffix != ".xlsx":
        raise ValueError("Output file must be an .xlsx file")
    output_file_path = input_file_path.parent / output_file_path
    if output_file_path.exists():
        output_file_path = input_file_path.parent / (
            output_file_path.stem + "_new" + output_file_path.suffix
        )

    return input_file_path, output_file_path


def main():
    args = args_parser()
    input_file_path, output_file_path = io(args.input, args.output)
    header = args.header

    df = pd.read_excel(input_file_path, header=0 if header else None)

    h1, h2 = df.columns[0], df.columns[1]

    # delete columns far from h1 and h2
    df = df.iloc[:, :2]

    # delete rows with empty values in h2
    df = df[df[h2].notna()]

    df[h1] = df[h1].str.upper()
    df[h2] = df.groupby(df[h1])[h2].transform(
        lambda y: "".join(
            sorted(
                list(set(y)),
                key=lambda x: (
                    x != "G",
                    x != "U",
                    x != "L",
                    x != "N",
                    x != "N(DNS)",
                ),
            )
        )
    )

    result = df.drop_duplicates()
    print(result.loc[:5])
    result.to_excel(output_file_path, index=False)


if __name__ == "__main__":
    main()
