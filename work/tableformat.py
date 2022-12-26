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
