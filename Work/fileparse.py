# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(file_obj, select=None, types=None, has_headers=True, delimiter=',', silence_errors=True):
    '''
    Parse a CSV file into a list of records
    '''
    rows = csv.reader(file_obj, delimiter=delimiter)

    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    #Read headers
    if has_headers:
        headers = next(rows)
    
    if select:
        indeces = [headers.index(colname) for colname in select]
        if has_headers:
            headers = select
    else:
        indeces = []

    records = []
    for rowNum, row in enumerate(rows, start=1):
        if not row: #skip empty rows
            continue
        
        try:
            if indeces:
                row = [row[index] for index in indeces]
            if types:
                row = [func(val) for func, val in zip(types, row)]

            if has_headers:
                records.append({name: value for name, value in zip(headers,row)})
            else:
                records.append(row)
        except ValueError as ve:
            if not silence_errors:
                print(f'Row {rowNum}: Couldn\'t convert {row}')
                print(f'Row {rowNum}: Reason {ve}')
    return records