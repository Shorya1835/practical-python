# fileparse.py
#
# Exercise 3.3
import csv
def parse_csv(filename,select=[],types=[],has_headers=True):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows=csv.reader(f)
        headers=[]
        if has_headers:
            headers=next(rows)
        records=[]
        if select:
            indices=[headers.index(colname) for colname in select]
        else:
            indices=[]
            
        for row in rows:
            if not row:
                continue
            if indices:
                row=[row[index] for index in indices]
            if types:
                row=[func(val) for func,val in zip(types,row)]
            if headers:
                record=dict(zip(headers,row))
            else:
                record=tuple(row)
            records.append(record)

    return records
