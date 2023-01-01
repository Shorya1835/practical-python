class TableFormatter:
  def headings(self,headers):
      for h in headers:
          print(f'{h:>10s}',end=' ')
      print()
      print(('-'*10 + ' ')*len(headers))
  def row(self,rowdata):
    for d in rowdata:
        print(f'{d:>10s}',end=' ')
    print()
class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format
    '''
    def headings(self,headers):
        print(','.join(headers))
        
    def row(self,rowdata):
        print(','.join(rowdata))
class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format
    '''
    def headings(self,headers):
        print(f"<tr><th>{'</th><th>'.join(headers)}</th><th>")
        
    def row(self,rowdata):
        print(f"<tr><td>{'</td><td>'.join(rowdata)}</td><td>")
class FormatError(Exception):
    pass
def create_formatter(fmt):
    if(fmt=='csv'):
        return CSVTableFormatter()
    elif(fmt=='HTML'):
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown format {fmt}')
        
def print_table(portfolio,columns,TbleFormatter):
    for s in columns:
        print(f'{s:>10s}',end=' ')
    print()
    print(('-'*10 + ' ')*len(columns))
    for d in portfolio:
        for c in columns:
            print(f'{getattr(d,c):>10}',end=' ')
        print()
