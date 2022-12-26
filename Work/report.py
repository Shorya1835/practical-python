# report.py
#
# Exercise 2.4
import csv
import fileparse
import sys
import stock
import tableformat
def read_portfolio(filename):
    with open(filename) as f:
        portfol=fileparse.parse_csv(f)
   
    portfolio=[stock.Stock(d['name'],d['shares'],d['price']) for d in portfol]
    return portfolio
def read_prices(filename) -> dict:
    '''
    Read prices from a CSV file of name,price data
    '''
    with open(filename) as f:
        price=fileparse.parse_csv(f,has_headers=False)
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
        totalcost+=s.shares*s.price
        totalvalue+=s.shares*prices[s.name]
        
    if totalcost<=totalvalue:
        print('retire')
    else:
        print('cannot retire')
        
def make_report(reportdata,formatter):
    formatter.headings(['Name','Shares','Price','Change'])
    for name,shares,price,change in reportdata:
        rowdata=[name,str(shares),f'{price:0.2f}',f'{change:0.2f}']
        formatter.row(rowdata)
def make_report_data(portfolio,prices):
    reportdata=[(s.name,int(s.shares),float(s.price),float(price[s.name]-s.price)) for s in portfolio]
def portfolio_report(fn1,fn2):
    portfolio=read_portfolio(fn1)
    prices=read_prices(fn2)
    make_report(portfolio,prices)
    
if(len(sys.argv) == 3):
    portfolio_report(sys.argv[1],sys.argv[2])
