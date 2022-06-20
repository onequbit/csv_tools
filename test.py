#!/usr/bin/python3
from argparse import ArgumentParser
from os.path import abspath, basename, isfile, split
import sys
from csv_tools import CSVInfo


class Main:
    def parsed_cmd_args():        
        cli = ArgumentParser(
            prog=(basename(__file__)),
            description='csv_tools module tester')
        cli.add_argument(
            "-f", "--filename", type=str, required=True,
            help="file to open from command line")
        cli.add_argument(
            "--header", default=False, action="store_true",
            help="indicate that the first row is a header row")
        
        result = cli.parse_args(sys.argv[1:])
        assert result.filename is not None, "please specify a file to open"
        assert isfile(result.filename), f"could not find {result.filename}"
        result.filename = abspath(result.filename)
        return result

    def run():
        parameters = Main.parsed_cmd_args()
        csv_file_test = CSVInfo(parameters.filename, parameters.header)
        print(csv_file_test)

if __name__ == "__main__":
    Main.run()
    