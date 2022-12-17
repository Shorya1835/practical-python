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
        for line in rows:
            try:
                sum+=int(line[1])*float(line[2])
            except ValueError:
                print("Couldn't parse",line,end='')
    return sum
    
if len(sys.argv)==2:
    filename=sys.argv[1]
else:
    filename='Data/portfolio.csv'

cost=portfolio_cost(filename)
print('Total cost:',cost)
