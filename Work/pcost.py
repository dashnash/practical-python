# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    cost = 0
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            try:
                cost += float(row[1]) * float(row[2])
            except ValueError as vE:
                print('Error in Line:', row)
                print(vE)
    
    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost('Data/missing.csv')
print('Total Cost: ' + str(cost))