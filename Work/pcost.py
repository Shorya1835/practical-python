# pcost.py
#
# Exercise 1.27
import csv
import sys
def portfolio_cost(filename):
    sum=0.0
    with open(filename,'rt') as f:
        rows=csv.reader(f)
        headers=next(rows)
        for n,line in enumerate(rows,start=1):
            record=dict(zip(headers,line))
            try:
                sum+=int(record['shares'])*float(record['price'])
            except ValueError:
                print(f"Row {n}: Couldn't convert: {line}")    
    return sum
    
if len(sys.argv)==2:
    filename=sys.argv[1]
else:
    filename='Data/portfolio.csv'

cost=portfolio_cost(filename)
print('Total cost:',cost)
