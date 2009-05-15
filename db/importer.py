#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import codecs
import pdb


class UTF8Recoder:
    """ Iterator that reads an encoded stream and reencodes the input to UTF-8 """
    
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)
    
    def __iter__(self):
        return self
    
    def next(self):
        return self.reader.next().encode("utf-8")

class UnicodeCSVReader:
    """ A CSV reader which will iterate over lines in the CSV file "f", which is encoded in the given encoding. """
    
    def __init__(self, f, dialect=csv.excel, encoding="utf-8", headers=[], **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)
        self.headers = headers
    
    def __iter__(self):
        return self

    def list2dict(fn):
        def new(self):
            list = fn(self)
            if len(self.headers) == len(list):
                dict = {}
                for header, value in zip(self.headers, list):
                    dict[header] = value
                return dict
            else:
                return list
        return new

    @list2dict
    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]
    

headers = ['1', 'l_name', 'f_name', 'p_name', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22']
with open('/home/alexey/Документы/БАД/Иркутск уичтеля.csv', 'rb') as f:
    ucsv = UnicodeCSVReader(f, headers=headers)
    for row in ucsv:
        print type(row)
        try:
            print u"Учитель: %s %s %s" % (row['l_name'], row['f_name'], row['p_name'])
        except Exception as e:
            print e

