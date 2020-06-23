# pcost.py
#
# Exercise 1.27
import csv
import sys
from report import read_portfolio

def portfolio_cost(filename):
    cost = 0
    portfolio = read_portfolio(filename)
    cost = sum([record['shares'] * record['price'] for record in portfolio])
    # with open(filename) as f:
    #     rows = csv.reader(f)
    #     headers = next(rows)
    #     for rowno, row in enumerate(rows):
    #         record = dict(zip(headers, row))
    #         try:
    #             nshares = int(record['shares'])
    #             price = float(record['price'])
    #             cost += nshares * price
    #         except ValueError as vE:
    #             print(f'Error in Line({rowno}): {row}')
    #             print(vE)
    
    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total Cost: ' + str(cost))