# report.py
#
# Exercise 2.4
import csv
from fileparse_v2 import parse_csv
import stock
import tableformat
from portfolio import Portfolio

def read_portfolio(filename, **options):
    with open(filename, 'rt') as f:
       self = Portfolio.from_csv(f, **options) 
    

    return self 

def read_prices(filename):
    with open(filename,'rt') as f:
        priceslist = parse_csv(f, types=[str,float], has_headers=False)
    prices = dict(priceslist) 
    return prices

def print_report(reportdata, formatter): 
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    header = (['Name', 'Share', 'Price', 'Change'])
    for name, share, price, change in reportdata:
        rowdata = [ name, str(share),  f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)
#    print('%10s %10s %10s %10s' % header)
#    print(('-' * 10 + ' ') * len(header))
#    for entry in portfolio:
#        name = entry.name
#        shares = entry.shares
#        price = entry.price
#        cur_price = prices[name]
#        change = cur_price - price
#        cur_price_s = f'${cur_price:.2f}'
#        print(f'{name:>10s} {shares:>10d} {cur_price_s:>10s} {change:>10.2f}')

def calculate_cost(portfolio, prices):
    '''
    Calculat the value of shares in portfolio,
    the gain, and print them out
    '''
    total = 0
    gain = 0
    for entry in portfolio:
        current_p = prices[entry.name]
        previous_p = entry.price
        share = entry.shares

        total += share * current_p
        gain += (current_p - previous_p) * share

	     
    print(f"The total values is {total:0.2f}, the gain is {gain:0.2f}")       

def make_reportdata(portfolio, prices):
    '''
    produce (name, shares, price, change) tuple from portfolio and prices
    '''
    records = []

    for entry in portfolio:
        name = entry.name
        shares = entry.shares
        price = entry.price
        cur_price = prices[name]
        change = cur_price - price
        records.append( (name, shares, cur_price, change))

    return records
 
def portfolio_report(portfolio_file='Data/portfolio.csv', prices_file='Data/prices.csv'):
    '''
    Present a report based on portfolio and prices
    '''
    
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    
    report = make_reportdata(portfolio, prices)
    
    formatter = tableformat.CSVTableFormatter()
 
    print_report(report, formatter)

def main(argv):
    portfolio_report(argv[1], argv[2])

if __name__ == '__main__':
    import sys
    # This file sets up basic configuration of the logging module.
    # Change settings here to adjust logging output as needed.
    import logging
    logging.basicConfig(
            filename = 'app.log',            # Name of the log file (omit to use stderr)
            filemode = 'w',                  # File mode (use 'a' to append)
            level    = logging.WARNING,      # Logging level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
            )


    main(sys.argv)
