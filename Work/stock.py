# Exercise 4.1
#
#
# stock.py
from typedproperty import typedproperty, String, Integer, Float

class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

#    __slots__ = ('name', '_shares', 'price')    
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'


    def sell(self, shares):
        self.shares -= shares

    @property
    def cost(self):
        return self.shares * self.price

