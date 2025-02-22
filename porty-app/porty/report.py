# report.py
#
# Exercise 2.4
import csv
from . import fileparse
import sys
from . import stock
from . import tableformat
from .portfolio import Portfolio

def read_portfolio(filename,**opts):
    with open(filename) as f:
        return Portfolio.from_csv(f)
    
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
    reportdata=[(s.name,int(s.shares),float(s.price),float(prices[s.name]-s.price)) for s in portfolio]
    return reportdata
def portfolio_report(fn1,fn2,fmt='HTML'):
    portfolio=read_portfolio(fn1)
    prices=read_prices(fn2)
    report=make_report_data(portfolio,prices)
    formatter=tableformat.create_formatter(fmt)
    make_report(report,formatter)
    
if(len(sys.argv) == 3):
    portfolio_report(sys.argv[1],sys.argv[2])
elif(len(sys.argv) == 4):
    portfolio_report(sys.argv[1],sys.argv[2],sys.argv[3])
