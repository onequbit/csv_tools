#!/usr/bin/python3

# csv_tools/__init__.py

from csv import Sniffer

def _get_dialect(filename):
    with open(filename, newline='') as csvfile:
        sniffer = Sniffer()
        return sniffer.sniff(csvfile.read(4096))

