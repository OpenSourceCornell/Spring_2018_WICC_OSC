import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')

import snow

class snowTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(snow.snow({"uris": 5, "olin": 3.4, "gates": 6}), "gates")
    
    def test2(self):
        self.assertEqual(snow.snow({"philips": 2}), "philips")
    
    def test3(self):
        self.assertEqual(snow.snow({"rose": 9.39, "anabel taylor": 12.1, "upson": 5.77}), "anabel taylor")

if __name__ == '__main__':
    unittest.main()