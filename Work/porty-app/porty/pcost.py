# pcost.py
#
# Exercise 1.27
import csv
import sys
from . import report 

def portfolio_cost(filename):
    total_cost = 0

    portfolio = report.read_portfolio(filename)


    return portfolio.total_cost 

def main(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'Data/portfolio.csv'

    cost = portfolio_cost(filename)
    print(f"Total cost {cost}")

if __name__ == '__main__':
    main(sys.argv)
