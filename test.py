#!/usr/bin/python3
from argparse import ArgumentParser
from os.path import abspath, basename, isfile, split
import sys
import csv_to_html

class Main:
    def parsed_cmd_args():        
        cli = ArgumentParser(
            prog=(basename(__file__)),
            description='csv_tools module tester')
        cli.add_argument(
            "-f", "--filename", type=str, required=True,
            help="file to open from command line")
        cli.add_argument(
            "--no-header", type=bool, default=False,
            help="skip the first row as the header")
        
        result = cli.parse_args(sys.argv[1:])
        assert result.filename is not None, "please specify a file to open"
        assert isfile(result.filename), f"could not find {result.filename}"
        result.filename = abspath(result.filename)
        return result

    def run():
        parameters = Main.parsed_cmd_args()
        rows = csv_to_html.get_rows(parameters.filename)
        for row in rows:
            print(row)

if __name__ == "__main__":
    Main.run()
    