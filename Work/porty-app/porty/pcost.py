# pcost.py
#
# Exercise 1.27
import csv
from .report import read_portfolio
from .portfolio import Portfolio

def portfolio_cost(filename):
    cost = 0
    portfolio = read_portfolio(filename)
    cost = portfolio.total_cost
    return cost


def main(args):
    cost = portfolio_cost(args[1])
    print(f'Total Cost: {cost:.2f}')

if __name__ == '__main__':
    import sys
    main(sys.argv)
