import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')

import stocks

class stocksTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(stocks.stocks([9.5, 3.4, 3.3, 5.6, 7.0], 50), [3.3, 7.0])
    
    def test2(self):
        self.assertEqual(stocks.stocks([2.9, 3.0, 5.0, 3.4, 2.2, 4.4], 3), [2.2, 4.4])
    
    def test3(self):
        self.assertEqual(stocks.stocks([100.3, 4.5, 34.5, 23.4, 6.8, 19.2], 0.7), [])

if __name__ == '__main__':
    unittest.main()