import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')

import text_score

class textTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(text_score.text_score("I love to eat hot dogs for breakfast, hot dogs for lunch, and even for dinner!", "hot", "for"), -1)
    
    def test2(self):
        self.assertEqual(text_score.text_score("java is the best programming language, java beats python", "java", "python"), 1)
    
    def test3(self):
        self.assertEqual(text_score.text_score("my my my your my mine my myanmar your yours your", "my", "your"), 2)

if __name__ == '__main__':
    unittest.main()