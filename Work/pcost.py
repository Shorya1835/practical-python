# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    sum=0.0
    with open(filename,'rt') as f:
        next(f)
        for line in f:
            pcost=line.split(',')
            sum+=int(pcost[1])*float(pcost[2])
    
    return sum
        
cost=portfolio_cost=('C:/Users/shory/OneDrive/Documents/GitHub/practical-pythons/Work/Data/portfolio.csv')
print('Total cost:',cost)
