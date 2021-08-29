# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    portfolio = [] 
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            record = dict(zip(header, row)) 
            holding = {}
            holding['name'] = record['name'] 
            holding['shares'] =  int(record['shares'])
            holding['price'] =  float(record['price'])
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    prices = {}
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError: 
                print("There is a IndexError!")
                continue

    return prices

def make_report(portfolio, prices): 
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
 
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

total = 0
gain = 0

for entry in portfolio:
    current_p = prices[entry['name']]
    previous_p = entry['price']
    share = entry['shares']

    total += share * current_p
    gain += (current_p - previous_p) * share

print(f"The total values is {total:0.2f}, the gain is {gain:0.2f}")
