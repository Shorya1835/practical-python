from .follow import follow
import csv
from . import report
from . import tableformat

        
def select_columns(rows,indices):
    for row in rows:
        yield [row[index] for index in indices]
        
def convert_types(rows,types):
    for row in rows:
         yield[func(val) for func,val in zip(types,row)]
       
def make_dicts(rows,headers):
        rows=(dict(zip(headers,rows)) for row in rows)
        return rows

def filter_symbols(rows,names):
        rows=(row for row in rows if row['name'] in names)
        return rows
        
def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows=select_columns(rows,[0,1,4])
    rows=convert_types(rows,[str,float,float])
    rows=make_dicts(rows,['name','price','change'])
    return rows

                
if __name__=='__main__':
    lines=follow('Data/stocklog.csv')
    rows=parse_stock_data(lines)
    for row in rows:
        print(row)

def ticker(portfolio,filename,format):
    portfolio=report.read_portfolio('Data/portfolio.csv')
    rows=parse_stock_data(follow('Data/stocklog.csv'))
    rows=filter_symbols(rows,portfolio)
    formatter=tableformat.create_formatter(format)
    formatter.headings(['Name','Price','Change'])
    for row in rows:
        formatter.row([ row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"] )
    
