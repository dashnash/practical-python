# stock.py
#
# Exercise 4.1
class Stock:
    'Class representing Stock unit'
    def __init__(self,name, shares, price):
        self.name=name
        self.shares=shares
        self.price=price

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price:0.2f})"
    
    def cost(self):
        'Calculates value of stock'
        return self.shares * self.price

    def sell(self, nShares):
        'sells nShares of stock'
        if nShares > self.shares:
            raise ValueError('nShares is more than the amount of shares')
        self.shares -= nShares