#!/usr/bin/python3

from argparse import ArgumentParser, BooleanOptionalAction
from os.path import abspath, basename, isfile, split
import csv
import sys

def _get_dialect(filename):
    with open(filename, newline='') as csvfile:
        sniffer = csv.Sniffer()
        return sniffer.sniff(csvfile.read(4096))

def get_rows(filename, no_header=False, options=None):
    import csv
    row_number = 0
    dialect = _get_dialect(filename)
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, dialect)
        if no_header:
            next(reader, None)
        for row in reader:
            yield row

class Main:
    def parsed_cmd_args():
        
        cli = ArgumentParser(
            prog=(basename(__file__)),
            description='csv_to_html : convert CSV data into HTML output')
        cli.add_argument(
            "-f", "--filename", type=str, required=True,
            help="file to open from command line")
        cli.add_argument(
            "--no-header", default=False, action="store_true",
            help="skip the first row as the header")
        
        result = cli.parse_args(sys.argv[1:])
        assert result.filename is not None, "please specify a file to open"
        assert isfile(result.filename), f"could not find {result.filename}"
        result.filename = abspath(result.filename)
        return result

    def run():
        parameters = Main.parsed_cmd_args()
        rows = get_rows(parameters.filename, no_header=parameters.no_header)
        for row in rows:
            print(row)
            

if __name__ == "__main__":
    Main.run()
    