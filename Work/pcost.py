# pcost.py
#
# Exercise 1.27
import csv
import sys
from report import read_portfolio

def portfolio_cost(filename):
    total_cost = 0

    portfolio = read_portfolio(filename)

    for record in portfolio:
        total_cost += record['shares'] * record['price']

    return total_cost

def main(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'Data/portfolio.csv'

    cost = portfolio_cost(filename)
    print(f"Total cost {cost}")

if __name__ == '__main__':
    main(sys.argv)
