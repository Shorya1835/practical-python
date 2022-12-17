# pcost.py
#
# Exercise 1.27
import csv
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
        
cost=portfolio_cost('Data/portfolio.csv')
print('Total cost:',cost)
