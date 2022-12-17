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
        headers=next(rows)
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
        totalcost+=s[1]*s[2]
    for t,s in prices,portfolio:
        totalvalue+=s[1]*t[1]
        
    if totalcost<=totalvalue:
        print('retire')
    else:
        print('cannot retire')
