# fileparse.py
#
# Exercise 3.3
from . import csv
from . import logging

log=logging.getLogger(__name__)

def parse_csv(f,select=[],types=[],has_headers=True,delimiter=',',silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not(has_headers):
        raise RuntimeError("select argument requires column headers")
        
    rows=csv.reader(f,delimiter=delimiter)
    headers=[]
    if has_headers:
        headers=next(rows)
    records=[]
    if select:
        indices=[headers.index(colname) for colname in select]
    else:
        indices=[]
            
    for i,row in enumerate(rows,start=1):
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
                log.warning("Row %d: Couldn't convert %s", i, row)
                log.debug("Row %d: Reason %s", i, e)

    return records
