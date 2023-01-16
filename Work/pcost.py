# pcost.py
#
# Exercise 1.27
import csv
import sys
import report
def portfolio_cost(filename):
    record=report.read_portfolio(filename)
    for n,line in enumerate(record,start=1):    
    return portfolio.total_cost
    
if len(sys.argv)==2:
    filename=sys.argv[1]
else:
    filename='Data/portfolio.csv'

cost=portfolio_cost(filename)
print('Total cost:',cost)
