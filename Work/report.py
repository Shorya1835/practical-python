# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    portfolio=[]
   
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding={'name':row[0],'shares':int(row[1]),'price':float(row[2])}
            portfolio.append(holding)
    return portfolio
def read_prices(filename):
    prices={}
    
    with open(filename,'rt') as f:
        rows=csv.reader(f)
        for row in rows:
            try:
                prices[row[0]]=float(row[1])
            except IndexError:
                None
     
    return prices
def retire():
    portfolio=read_portfolio('Data/portfolio.csv')
    prices=read_prices('Data/prices.csv')
    totalcost=0.0
    totalvalue=0.0
    for s in portfolio:
        totalcost+=s['shares']*s['price']
        totalvalue+=s['shares']*prices[s['name']]
        
    if totalcost<=totalvalue:
        print('retire')
    else:
        print('cannot retire')
        
def make_report(portfolio,prices):
    print('      Name     Shares      Price     Change')
    print('---------- ---------- ---------- ----------')
    for s in portfolio:
        print(f"{s['name']:>10s} {s['shares']:>10d} {s['price']:>10.2f} {(price[s['name']]-s['price']):>10.2f}")
    
