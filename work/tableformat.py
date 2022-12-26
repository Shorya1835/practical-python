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
        print('<tr><th>','</th><th>'.join(headers),'</th><th>')
        
    def row(self,rowdata):
        print('<tr><td>','</td><td>'.join(rowdata),'</td><td>')
