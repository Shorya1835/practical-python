# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    sum=0.0
    with open(filename,'rt') as f:
        next(f)
        for line in f:
            pcost=line.split(',')
            try:
                sum+=int(pcost[1])*float(pcost[2])
            except ValueError:
                print("Couldn't parse",line,end='')
    return sum
        
cost=portfolio_cost('Data/portfolio.csv')
print('Total cost:',cost)
