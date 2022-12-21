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
        for n,row in enumerate(rows):
            try:
                prices[row[0]]=float(row[1])
            except IndexError:
                print(f"Row {n}: Couldn't convert: {row}")     
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
    headers=('Name','Shares','Price','Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f"{' ':->11s}{' ':->11s}{' ':->11s}{' ':->11s}")
    for s in portfolio:
        print(f"{s['name']:>10s} {s['shares']:>10d} {('$'+'{:0.2f}'.format(prices[s['name']])):>10s} {(prices[s['name']]-s['price']):>10.2f}")
    
