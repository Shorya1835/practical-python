class Stock:
    def __init__ (self,name,shares,price):
        self.name=name
        self.shares=int(shares)
        self.price=float(price)
    @property
    def shares(self):
        return self._shares
    @shares.setter
    def shares(self,value):
        if not isinstance(value,int)
            raise TypeError('Expected int')
        self._shares = value
    @property
    def cost(self):
        return self.shares*self.price
    def sell(self,x):
        self.shares=self.shares-x
    def __repr__(self):
        return f'Stock({self.name},{self.shares},{self.price})'
class MyStock(Stock):
    def __init__(self,name,shares,price,factor):
        super().__init__(name,shares.price)
        self.factor = factor
    def panic(self):
        self.sell(self.shares)
        
    def cost(self):
        actual_cost = super().cost()
        return 1.25*actual_cost
