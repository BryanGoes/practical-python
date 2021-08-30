# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=[], types=[], has_headers=True,delimiter=','): 
    '''
    Parse csv files into a list of dictionary records
    '''
    records = []  

    with open(filename, 'rt') as f:
        rows = csv.reader(f, delimiter=delimiter)
        if has_headers:
	    headers = next(rows)
        
	    if not select: # if the select is none
		select = headers

	    types_all = ['str'] * len(headers)

	    if types: 
		indexs = [ headers.index(entry) for entry in select ]
		for i, each in zip(indexs, types):
		    types_all[i] = each
               
	    for row in rows:
		if not row:
		    continue
		records.append( {name:func(val) for name, val, func in zip(headers, row, types_all) if name in select})
        else:
            for row in rows:
	        if not row:
		    continue
                if types: 	
                    row = [ func(val) for func, val in zip(types, row) ]
                    record = tuple(row)
		    records.append(record)
                else:
                    records.append( (val for val in row))

    return records
