# report.py
#
# Exercise 2.4
import csv
import sys
from fileparse import parse_csv

types_headers = {
    'name' : str,
    'date' : str,
    'time' : str,
    'shares': int,
    'price': float
}

def read_portfolio(filename):
    select=['name', 'shares', 'price']
    portfolio = parse_csv(filename, select=select, 
        types=[types_headers[type_name] for type_name in select])

    return portfolio

def read_prices(filename):
    'reads set of stock prices from filename and returns a dictionary'
    price_tuples = parse_csv(filename, types=[str, float], has_headers=False)
    prices = {tup[0] : tup[1] for tup in price_tuples}

    return prices

def make_report(portfolio, prices):
    'Generates formatted report from portfolio and prices'
    report = []
    for holding in portfolio:
        report.append((holding['name'], holding['shares'], holding['price'], prices[holding['name']] - holding['price']))
    
    return report


def print_report(report):
    report_headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % report_headers)
    print(('-' * 10 + ' ') * len(report_headers))
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:10d} {f"${price}":>10s} {change:10.2f}')

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

portfolio_report('Data/portfolio.csv', 'Data/prices.csv')