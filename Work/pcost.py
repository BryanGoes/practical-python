# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    total_cost = 0

    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows) # get rid of header 
        for i,line in enumerate(rows,start=2):
            record = dict(zip(header, line))
            try:
                shares = int(record['shares'])
                price = float(record['price'])
                total_cost += shares * price

            except ValueError:
                print(f"Row {i}: Bad Row:{line}")
                continue
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f"Total cost {cost}")
