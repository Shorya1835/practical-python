# fileparse.py
#
# Exercise 3.3
import csv
def parse_csv(filename,select=[],types=[],has_headers=True,delimiter=',',silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not(has_headers):
        raise RuntimeError("select argument requires column headers")
    with open(filename) as f:
        rows=csv.reader(f,delimiter=delimiter)
        headers=[]
        if has_headers:
            headers=next(rows)
        records=[]
        if select:
            indices=[headers.index(colname) for colname in select]
        else:
            indices=[]
            
        for i,row in enumerate(rows):
            try:
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
            except ValueError as e:
                if not(silence_errors):
                    print(f"Row {i}: Couldn't convert {row}")
                    print(f'Row {i}: {e}')

    return records
