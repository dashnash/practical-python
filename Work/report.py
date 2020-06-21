# report.py
#
# Exercise 2.4
import csv
import sys

def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            try:
                portfolio.append(dict(zip(header, row)))
            except ValueError as vE:
                print('Error in Line:', row)
                print(vE)
    
    return portfolio

def read_prices(filename):
    'reads set of stock prices from filename and returns a dictionary'
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                name, price = row
                prices[name] = float(price)
            except ValueError as vE:
                print('Error:', row)
                print(vE)

    return prices

def make_report(portfolio, prices):
    'Generates formatted report from portfolio and prices'
    report = []
    for holding in portfolio:
        report.append((holding['name'], holding['shares'], holding['price'], prices[holding['name']] - float(holding['price'])))
    
    return report


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

portfolio = read_portfolio(filename)
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')

print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))

for name, shares, price, change in report:
    print(f'{name:>10s} {shares:10s} {f"${price}":>10s} {change:10.2f}')

# curr_value = 0.0
# acq_value = 0.0
# for holding in portfolio:
#     acq_value += holding['shares'] * holding['value']
#     curr_value += prices[holding['name']] * holding['shares']

# print('Current Value:', curr_value)

# change = curr_value - acq_value
# change_str = '$'+ str(change)
# if change < 0.0:
#     change_str = '$(' + str(-1 * change) + ')'

# print('Gain/Loss:', change_str)
