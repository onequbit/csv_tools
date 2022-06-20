#!/usr/bin/python3

import csv, json

class CSVInfo(dict):
    WHIFF = 4096
    def __init__(self, filename, has_header=None):
        self.filename = filename        
        self.file_handle = open(self.filename, newline='')
        sniffer = csv.Sniffer()
        self.dialect = sniffer.sniff(self.file_handle.read(self.WHIFF))
        self.reset()
        if has_header:
            self.has_header = has_header
        else:
            self.has_header = sniffer.has_header(self.file_handle.read(self.WHIFF))
        self.reset()
        self.reader = csv.reader(self.file_handle, self.dialect)
        dict.__init__(
            self, 
            filename=self.filename, 
            file_handle=self.file_handle,
            dialect=self.dialect,
            has_header=self.has_header,
            reader=self.reader
        )

    def reset(self):    
        self.file_handle.seek(0,0)

    def skip_header(self):
        if self.has_header:
            self.reset
            _ = self.file_handle.readline()

    def get_rows(self):
        for row in self.reader:
            yield row