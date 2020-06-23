# ticker.py

from follow import follow
from tableformat import create_formatter, print_table
from report import read_portfolio
import csv

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = (dict(zip(['name', 'price','change'], row)) for row in rows)
    return rows

def select(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def ticker(portfile, logfile, fmt):
    portfolio = read_portfolio(portfile)
    formatter = create_formatter(fmt)
    lines = follow(logfile)
    rows = parse_stock_data(lines)
    rows = (row for row in rows if row['name'] in portfolio)
    formatter.headings(["Name", "Price", "Change"])
    for row in rows:
        formatter.row([row['name'], str(row['price']), str(row['change'])])

if __name__ == '__main__':
    ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'txt')