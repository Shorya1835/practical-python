# report.py
#
# Exercise 2.4
import csv
import fileparse

def read_portfolio(filename):
    portfolio=fileparse.parse_csv(filename)
   
    for row in portfolio:
        row['shares']=int(row['shares'])
        row['price']=float(row['price'])
    return portfolio
def read_prices(filename) -> dict:
    '''
    Read prices from a CSV file of name,price data
    '''
    price=fileparse.parse_csv(filename)
    prices={}
    for key,value in price:       
        try:
            prices[key]=float(value)
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
    headers=('Name','Shares','Price','Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f"{' ':->11s}{' ':->11s}{' ':->11s}{' ':->11s}")
    for s in portfolio:
        print(f"{s['name']:>10s} {s['shares']:>10d} {('$'+'{:0.2f}'.format(prices[s['name']])):>10s} {(prices[s['name']]-s['price']):>10.2f}")

def portfolio_report(fn1,fn2):
    portfolio=read_portfolio(fn1)
    prices=read_prices(fn2)
    make_report(portfolio,prices)
