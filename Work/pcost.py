# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    total_cost = 0

    with open(filename) as f:
        rows = csv.reader(f)
        next(rows) # get rid of header 
        for line in rows:
            try:
                shares = int(line[1])
            except ValueError:
                print("The field is possibly missing! Check your raw data!")
                continue
            price = float(line[2])
            total_cost += shares * price
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f"Total cost {cost}")
