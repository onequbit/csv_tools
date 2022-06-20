#!/usr/bin/python3

from argparse import ArgumentParser, BooleanOptionalAction
from os.path import abspath, basename, isfile, split
import csv
import sys
from library import _get_dialect

# def _get_dialect(filename):
#     with open(filename, newline='') as csvfile:
#         sniffer = csv.Sniffer()
#         return sniffer.sniff(csvfile.read(4096))

def has_header(filename):
    with open(filename, newline='') as csvfile:
        sniffer = csv.Sniffer()
        return sniffer.has_header(csvfile.read(4096))

def get_columns(filename):
    import csv
    if not has_header:
        raise Exception("no header to read")
    
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
        rows = get_columns(parameters.filename)
        for row in rows:
            print(row)
            

if __name__ == "__main__":
    Main.run()
    