#Exercise 6.10
#
#
#ticker.py
from . import follow 
import csv
from . import report
from . import tableformat

def select_column(rows, indices):
    for row in rows:
        yield [ row[index] for index in indices ]

def convert_types(rows, types):
    for row in rows:
        yield [ fun(val) for fun, val in zip(types, row) ]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row 
            
def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_column(rows, [0,1,4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def ticker(portfile, logfile, fmt, names):
    portfolio = report.read_portfolio(portfile)
    rows = parse_stock_data(follow.follow(logfile))
    rows = ( row for row in rows if row['name'] in names) 
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(["Name", "Price", "Change" ])
    for row in rows:
        formatter.row([ row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"])

if __name__ == '__main__':
    lines = follow.follow('Data/stocklog.csv')
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)
