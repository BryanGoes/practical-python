#Another concise version of parsing files
import csv

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',',silence_errors=False):
    records = []
    if (not has_headers) and select:
        raise RuntimeError('select argument requires column headers')
    if isinstance(lines,str):
        raise RuntimeError('the lines should not be string!')
        sys.exit(1) 

    rows = csv.reader(lines, delimiter=delimiter)
    headers = next(rows) if has_headers else []

    if select:
        index = [ headers.index(i) for i in select ]
        headers = select

    for i,row in enumerate(rows, start=1):
        if not row:
            continue
	
        if select:
            row = [ row[i] for i in index ]
        
        if types:
            try:
                row = [ func(val) for func, val in zip(types, row) ]
            except ValueError:
                if silence_errors:
                    pass
                else:
                    print(f'Row {i}: couldn\'t convert {row} ')
        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)

        records.append(record)  

    return records
