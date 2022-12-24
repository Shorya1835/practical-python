# fileparse.py
#
# Exercise 3.3
import csv
def parse_csv(filename,select=[]):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows=csv.reader(f)
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
            record=dict(zip(headers,row))
            records.append(record)

    return records
