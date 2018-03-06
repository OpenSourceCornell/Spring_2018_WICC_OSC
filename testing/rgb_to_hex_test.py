import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')

import rgb_to_hex

class rgbTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(rgb_to_hex.rgb_to_hex(5, 45, 67), "#052D43")
    
    def test2(self):
        self.assertEqual(rgb_to_hex.rgb_to_hex(255, 255, 255), "#FFFFFF")
    
    def test3(self):
        self.assertEqual(rgb_to_hex.rgb_to_hex(23, 0, 0), "#170000")

if __name__ == '__main__':
    unittest.main()