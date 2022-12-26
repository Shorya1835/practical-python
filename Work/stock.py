class Stock:
    def __init__ (self,name,shares,price):
        self.name=name
        self.shares=int(shares)
        self.price=float(price)
    def cost(self):
        return self.shares*self.price
    def sell(self,x):
        self.shares=self.shares-x
class MyStock(Stock):
    def panic(self):
        self.sell(self.shares)
        
    def cost(self):
        actual_cost = super().cost()
        return 1.25*actual_cost
