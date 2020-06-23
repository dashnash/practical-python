# report.py
#
# Exercise 2.4
import csv
from fileparse import parse_csv
from stock import Stock
import tableformat

types_headers = {
    'name' : str,
    'date' : str,
    'time' : str,
    'shares': int,
    'price': float
}

def read_portfolio(filename):
    select=['name', 'shares', 'price']
    with open(filename) as f:
        port_dict = parse_csv(f, select=select, 
            types=[types_headers[type_name] for type_name in select])
        
        portfolio = [Stock(record['name'], record['shares'], record['price'])
            for record in port_dict]

    return portfolio

def read_prices(filename):
    'reads set of stock prices from filename and returns a dictionary'
    with open(filename) as f:
        price_tuples = parse_csv(f, types=[str, float], has_headers=False)
    
    prices = {tup[0] : tup[1] for tup in price_tuples}

    return prices

def make_report(portfolio, prices):
    'Generates formatted report from portfolio and prices'
    report = []
    for holding in portfolio:
        report.append((holding.name, holding.shares, holding.price, prices[holding.name] - holding.price))
    
    return report


def print_report(report, formatter):
    'Prints a report'
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)

def portfolio_report(portfolio_filename, prices_filename):
    'Generates and prints a report from the given filenames'
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices) 
    formatter = tableformat.TextTableFormatter()
    print_report(report,formatter)


def main(args):
    portfolio_report(args[1], args[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)