# pcost.py
#
# Exercise 1.27
sum=0.0
with open('C:/Users/shory/OneDrive/Documents/GitHub/practical-pythons/Work/Data/portfolio.csv','rt') as f:
    next(f)
    for line in f:
        pcost=line.split(',')
        sum+=int(pcost[1])*float(pcost[2])
    
    print('Total cost',sum)
