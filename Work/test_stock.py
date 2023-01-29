import unittest
import stock

class TestStock(unittest.TestCase):
  def test_create(self):
    s=stock.Stock('GOOG',100,490.1)
    self.assertEqual(s.name,'GOOG')
    self.assertEqual(s.shares,100)
    self.assertEqual(s.price,490.1)
    self.assertEqual(s.cost(),s.price*s.shares)'
    self.assert s.sell(2)
    
if __name__=='__main__':
  unittest.main()
