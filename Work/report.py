# report.py
#
# Exercise 2.4
import csv
from fileparse_v2 import parse_csv

def read_portfolio(filename):
    with open(filename, 'rt') as f:
        portfolio = parse_csv(f ,select=['name','shares','price'], types=[str,int,float])
    return portfolio

def read_prices(filename):
    with open(filename,'rt') as f:
        priceslist = parse_csv(f, types=[str,float], has_headers=False)
    prices = dict(priceslist) 
    return prices

def print_report(portfolio, prices): 
    header = ('Name', 'Share', 'Price', 'Change')
    print('%10s %10s %10s %10s' % header)
    print(('-' * 10 + ' ') * len(header))
    for entry in portfolio:
        name = entry['name']
        shares = entry['shares']
        price = entry['price']
        cur_price = prices[name]
        change = cur_price - price
        cur_price_s = f'${cur_price:.2f}'
        print(f'{name:>10s} {shares:>10d} {cur_price_s:>10s} {change:>10.2f}')
 
def calculate_cost(portfolio, prices):
    '''
    Calculat the value of shares in portfolio,
    the gain, and print them out
    '''
    total = 0
    gain = 0
    for entry in portfolio:
        current_p = prices[entry['name']]
        previous_p = entry['price']
        share = entry['shares']

        total += share * current_p
        gain += (current_p - previous_p) * share

	     
    print(f"The total values is {total:0.2f}, the gain is {gain:0.2f}")       

def portfolio_report(portfolio_file='Data/portfolio.csv', prices_file='Data/prices.csv'):
    '''
    Present a report based on portfolio and prices
    '''
    
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    
    print_report(portfolio, prices)

def main(argv):
    portfolio_report(argv[1], argv[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)
